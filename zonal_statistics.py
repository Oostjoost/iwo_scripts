#import de juiste libraries
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import glob, os, qgis.analysis

layer_list = []
qfd = QFileDialog()
title = 'Select directory'
path = "/Users"

#Get directory with .tiff files
f = QFileDialog.getExistingDirectory(qfd, title, path)

#initialize
os.chdir(f)
lyr = None
layer_list = []
layers = []

#Get BAG layer
title = 'Select BAG file'
bag_file = QFileDialog.getOpenFileName(qfd, title, f)
vectorlayer = iface.addVectorLayer(bag_file, "bag", "ogr")

#let's do all the calculations
for lyr in glob.glob("*.tif"):
    layer_name, ext = lyr.split(".")
    layer_list.append(layer_name)
    layers.append(lyr)
    qgis.analysis.QgsZonalStatistics(vectorlayer, lyr, attributePrefix=lyr, rasterBand=1).calculateStatistics(None)

#add all the raster layers
for i in range(len(layers)):
    iface.addRasterLayer(layers.pop())

#calculate time in BAG layer
vectorlayer.startEditing()

#step 1
myField = QgsField( 'tijdstip', QVariant.String)
vectorlayer.dataProvider().addAttributes([myField])
vectorlayer.updateFields()
idx = vectorlayer.fieldNameIndex( 'tijdstip' )

#step 2
xpression = 'CASE WHEN "t01.tifmea" > 0.1 THEN ' + "'01:00:00'" + ' WHEN "t02.tifmea" > 0.1 THEN ' + "'02:00:00'" + ' WHEN "t03.tifmea" > 0.1 THEN ' + "'03:00:00'" + '\
                 WHEN "t04.tifmea" > 0.1 THEN ' + "'04:00:00'" + ' WHEN "t05.tifmea" > 0.1 THEN ' + "'05:00:00'" + ' WHEN "t06.tifmea" > 0.1 THEN ' + "'06:00:00'" + '\
                 WHEN "t12.tifmea" > 0.1 THEN ' + "'12:00:00'" + ' WHEN "t24.tifmea" > 0.1 THEN ' + "'24:00:00'" + ' WHEN "t36.tifmea" > 0.1 THEN ' + "'36:00:00'" + '\
                 WHEN "t48.tifmea" > 0.1 THEN ' + "'48:00:00'" + ' WHEN "t60.tifmea" > 0.1 THEN ' + "'60:00:00'" + ' WHEN "t72.tifmea" > 0.1 THEN ' + "'72:00:00'" + 'END'
e = QgsExpression(xpression)
e.prepare(vectorlayer.pendingFields() )

for f in vectorlayer.getFeatures():
    f[idx] = e.evaluate( f )
    vectorlayer.updateFeature( f )

vectorlayer.commitChanges()