# -*- coding: utf-8 -*-

'''
Для активного слоя создается новое поле "fieldname".
Для каждого выделенного объекта слоя в поле "fieldname"
записывается единица.
'''

from qgis.core import *
from qgis.utils import *
from PyQt4.QtCore import *

layer = iface.activeLayer()

# если нужно создать новое поле:
layer.dataProvider().addAttributes([QgsField("fieldname", QVariant.Int)])

layer.startEditing()

selection = layer.selectedFeatures()

for feature in selection:
    #запись в поле 'fieldname' значения 1
    feature['fieldname'] = 1
    layer.updateFeature(feature)
    
layer.commitChanges()