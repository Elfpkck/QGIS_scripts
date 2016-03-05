#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Cкрипт выделяет притоки всех порядков выделенной реки.
The script selects all inflows of selected river.

Недостаток: другая река или приток другой реки также будут выделены, если они 
находятся слишком близко (пересекают минимальный прямоугольник, в который 
вписана изначально выделенная река и (или) ее приток).
'''
from qgis.core import *
from qgis.utils import *

layer = iface.activeLayer()
geom_ids = []

def inflower(line, set):
    for item in set.copy():
        if item.geometry().intersects(line.geometry().boundingBox()):
            geom_ids.append(item.id())
            set.remove(item)
            inflower(item, set)
    layer.select(geom_ids)

for selected in layer.selectedFeatures():
    river = selected

features = set()
for feature in layer.getFeatures():
    if river.id() != feature.id():
        features.add(feature)
        
inflower(river, features)

features.clear()
geom_ids = []