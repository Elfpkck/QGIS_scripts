#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Скрипт выделяет все полигоны данного слоя, углы при вершинах которых
не прямые.
This script selects all polygons of current layer if angles of
polygons doesn't 90 degrees.
'''
from qgis.core import *
from qgis.utils import *
layer = iface.activeLayer()
dict = {}
for polygon in layer.getFeatures():
    c = []
    z = []
    a = []
    for node in polygon.geometry().asPolygon()[0]:
        a.append(node)
    line = QgsGeometry.fromPolyline(a)

    x = 0
    while x < len(line.asPolyline()) - 1:
        line_start = QgsPoint(line.asPolyline()[x])
        line_end = QgsPoint(line.asPolyline()[x+1])
        c.append(line_start.azimuth(line_end))
        x += 1
    
    x = 0
    while x < len(c) - 1:
        z.append(round(abs(c[x] - c[x+1])))
        if x == len(c) - 2:
            z.append(round(abs(c[x+1] - c[0])))
        x += 1
    d = {polygon.id(): z}
    dict.update(d)

sel = []
for key in dict:
    for i in dict.get(key):
        if (int(i) % 90) != 0:
            sel.append(key)

layer.select(sel)