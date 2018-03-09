from PyQt4.QtGui import *
from PyQt4.QtCore import *
from qgis.PyQt.QtXml import QDomDocument
from qgis.utils import iface
#import time

def get_layer_by_name(layer_name):
    layer = None
    for lyr in QgsMapLayerRegistry.instance().mapLayers().values():
        if lyr.name() == layer_name:
            layer = lyr
    return layer

for lyr in QgsMapLayerRegistry.instance().mapLayers().values():
    iface.legendInterface().setLayerVisible(lyr, False)

tijdDict = {0: '00', 1: '01', 2: '02', 3: '03', 4: '04', 5: '05', 6: '06', 7: '12', 8: '24', 9: '36', 10: '48', 11: '60', 12: '72'}
canvas = iface.mapCanvas()
layer_list = ["kwetsbare_objecten", "doorbraaklocaties uit coordinatieplan", "bag", "liander_leidingen",  "brtachtergrondkaart"]

aantal = 0

qid = QInputDialog()
while True:
    aantal, ok = QInputDialog.getInt(qid, "Aantal keer:", "Hoeveel Rasterlagen bevat dit scenario?", QLineEdit.Normal,)
    if aantal != 0:
        break
        
qfd = QFileDialog()
title = 'Select directory to save png files'
path = "/Users"
f = QFileDialog.getExistingDirectory(qfd, title, path)

title = 'Select print sjabloon'
printSjabloon = QFileDialog.getOpenFileName(qfd, title, f, "*.qpt")
 
for i in range(aantal):
    layerSettings = []
    printTemplatePath = printSjabloon
    template_file = file(printTemplatePath)
    template_content = template_file.read()
    template_file.close()
    document = QDomDocument()
    document.setContent(template_content)
    for lyr in QgsMapLayerRegistry.instance().mapLayers().values():
        if lyr.name() not in layer_list:
            iface.legendInterface().setLayerVisible(lyr, False)
        else:
            iface.legendInterface().setLayerVisible(lyr, True)
    name = "t" + tijdDict[i]
    tijd = "'" + tijdDict[i] + ":00:00'"
    printTijd = tijdDict[i] + ":00"
        
    for lyr in layer_list:
        tempLayer = get_layer_by_name(lyr)
        layerSettings.append(tempLayer.id())      
    if i > 0:
        rasterLayer = get_layer_by_name(name)
        netwerkLayer = get_layer_by_name("liander_" + name + "_leidingen")
        iface.legendInterface().setLayerVisible(rasterLayer, True)
        iface.legendInterface().setLayerVisible(netwerkLayer, True)
        layerSettings[4:4] = [rasterLayer.id()]
        layerSettings[1:1] = [netwerkLayer.id()]
    bagLayer = get_layer_by_name("bag")
    sub_string = '"tijdstip" <= ' + tijd +  " and " + '"tijdstip" is not null'
    bagLayer.setSubsetString(sub_string)

    settings = canvas.mapSettings()
    settings.setLayers(layerSettings)
    composition = QgsComposition(settings)

    composition.loadFromTemplate(document, {})
    
    time_item = composition.getComposerItemById('tijdstip')
    time_item.setText(printTijd)

    composition.refreshItems()
    imagePath = f + '/' + name + '.png'
    dpi = composition.printResolution()
    dpmm = dpi / 25.4
    width = int(dpmm * composition.paperWidth())
    height = int(dpmm * composition.paperHeight())
    image = QPixmap(QSize(width, height))
    imagePainter = QPainter(image)
    sourceArea = QRectF(0, 0, composition.paperWidth(), composition.paperHeight())
    targetArea = QRectF(0, 0, width, height)
    composition.render(imagePainter, targetArea, sourceArea)
    imagePainter.end()
    image.save(imagePath,'png')