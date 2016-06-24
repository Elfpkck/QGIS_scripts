#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Script finds minimal distances between points and line or polygon. 
Value of distance is added (overwritted) to field "Dist" of point attribute table. 
In linear or polygonal layer must be 1 object.
In table of content must be 2 layers.
"""

from PyQt4.QtCore import QVariant
from qgis.core import *
from qgis.utils import *

layers = QgsMapLayerRegistry.instance().mapLayers().values()
for layer in layers:
    if layer.type() == QgsMapLayer.VectorLayer and layer.wkbType() == QGis.WKBPoint:
        point_layer = layer       
    if layer.type() == QgsMapLayer.VectorLayer and layer.wkbType() == (QGis.WKBPolygon or QGis.WKBLineString):    
        lp_layer = layer
       
for point in point_layer.getFeatures():
    try:
        point['dist']
        break
    except KeyError:
        point_layer.dataProvider().addAttributes([QgsField("dist", QVariant.Int)])
        break
        
with edit(point_layer): 
    for line in lp_layer.getFeatures():
        for point in point_layer.getFeatures():
            distance = line.geometry().distance(point.geometry())
            print distance
            distance = int(distance)
            point['dist'] = distance
            point_layer.updateFeature(point)
    
