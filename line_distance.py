#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
В списке distance_list указываются расстояния, 
координаты которых необходимо получить. 
Расстояния откладываются от начала линии. 
'''

from qgis.core import *
from qgis.utils import *

layer = iface.activeLayer()
distance_list = [
118225,
150593,
165534,
174645,
176059,
179604.5,
184062,
200730
]

for item in distance_list:
    for line in layer.getFeatures():
        print line.geometry().interpolate(item).asPoint()
