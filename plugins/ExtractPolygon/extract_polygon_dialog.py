# -*- coding: utf-8 -*-
"""
/***************************************************************************
 ExtractPolygonDialog
                                 A QGIS plugin
 extract polgon based on color from geotiff
                             -------------------
        begin                : 2018-02-21
        git sha              : $Format:%H$
        copyright            : (C) 2018 by Joost Deen
        email                : jdeen@vrnhn.nl
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

from PyQt4.QtGui import *
from PyQt4.QtCore import *
from qgis.core import QgsMapLayerRegistry, QgsVectorFileWriter
import glob, os, processing
from qgis.analysis import QgsRasterCalculator, QgsRasterCalculatorEntry
from processing.tools import *

from PyQt4 import QtGui, uic

FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'extract_polygon_dialog_base.ui'))

class ExtractPolygonDialog(QtGui.QDialog, FORM_CLASS):

    check_input = 0
    iface = None
    inputFile = None
    outputFile = None

    def __init__(self, parent=None):
        """Constructor."""
        super(ExtractPolygonDialog, self).__init__(parent)
        self.setupUi(self)
        self.get_geotiff.clicked.connect(self.get_input_file)
        self.red_spinBox.valueChanged.connect(lambda: self.spinbox_changed(who = 'red'))
        self.green_spinBox.valueChanged.connect(lambda: self.spinbox_changed(who = 'green'))
        self.blue_spinBox.valueChanged.connect(lambda: self.spinbox_changed(who = 'blue'))
        self.red_slider.sliderMoved.connect(lambda: self.slider_changed(who = 'red'))
        self.green_slider.sliderMoved.connect(lambda: self.slider_changed(who = 'green'))
        self.blue_slider.sliderMoved.connect(lambda: self.slider_changed(who = 'blue'))
        self.runButton.clicked.connect(self.run)
        self.runButton.setEnabled(False)
        
    def qgs_map_calculator(self, rasterLayer, temp_path, red, green, blue):
        entries = []
        # Define 3 bands
        
        rasterFilterQgs = '( temp@1 = ' + str(red) + 'AND temp@2 = ' + str(green) + 'AND temp@3 = ' + str(blue) + ') * 1'
        for i in range(3):
            ent = QgsRasterCalculatorEntry()
            ent.ref = 'temp@' + str(i + 1)
            ent.raster = rasterLayer
            ent.bandNumber = i + 1
            entries.append( ent )
        file = temp_path + '/temp_qgs.tif'
        calc = QgsRasterCalculator( rasterFilterQgs, 
                            file, 
                            'GTiff',
                            rasterLayer.extent(), 
                            rasterLayer.width(), 
                            rasterLayer.height(), 
                            entries )
        calc.processCalculation()
        return file       

    def saga_map_calculator(self, tempLayer):
        rasterFilterSaga = 'ifelse(g1 = 0, 0/0, g1)'
        output_alg = processing.runandload('saga:rastercalculator', tempLayer , [], rasterFilterSaga, 0, False, 7, None)
        
    def gdal_polygonize(self, layer, f):
        #output_file = f + '/temp_pol.shp'
        result = processing.runandload('gdalogr:polygonize', layer, "DN", "output")
        
    def get_layer_by_name(self, layer_name):
        layer = None
        for lyr in QgsMapLayerRegistry.instance().mapLayers().values():
            if lyr.name() == layer_name:
                layer = lyr
        return layer
        
    def get_input_file(self):
        qfd = QFileDialog()
        title = 'Select Georeferenced .tif file'
        path = str(os.path)
        self.inputFile = QFileDialog.getOpenFileName(qfd, title, path)
        if self.inputFile != None:
            self.check_input = 1
            self.input_geotiff.setText(str(self.inputFile))
        else:
            self.check_input = 1
        if self.check_input == 1:
            self.runButton.setEnabled(True)  

    def run(self):
        #first initialize the variables
        #colors to be extracted in rgb
        red = self.red_spinBox.value()
        green = self.green_spinBox.value()
        blue = self.blue_spinBox.value()
        temp_path = os.environ['TEMP']
        
        rasterLayer = self.iface.addRasterLayer(self.inputFile)
        tempFile = self.qgs_map_calculator(rasterLayer, temp_path, red, green, blue)
        
        tempRasterLayer = self.iface.addRasterLayer(tempFile)
        self.saga_map_calculator(tempRasterLayer)

        QgsMapLayerRegistry.instance().removeMapLayer(rasterLayer.id())
        QgsMapLayerRegistry.instance().removeMapLayer(tempRasterLayer.id())

        layer_name = 'Calculated'
        layer = self.get_layer_by_name(layer_name)
        self.gdal_polygonize(layer, temp_path)
        QgsMapLayerRegistry.instance().removeMapLayer(layer.id())
        
        self.close()
        del self

    def spinbox_changed(self, who):
        if who == 'red':
            self.red_slider.setValue(self.red_spinBox.value())
        if who == 'green':
            self.green_slider.setValue(self.green_spinBox.value())
        if who == 'blue':
            self.blue_slider.setValue(self.blue_spinBox.value())
        
    def slider_changed(self, who):
        if who == 'red':
            self.red_spinBox.setValue(self.red_slider.value())
        if who == 'green':
            self.green_spinBox.setValue(self.green_slider.value())
        if who == 'blue':
            self.blue_spinBox.setValue(self.blue_slider.value())

        