# -*- coding: utf-8 -*-

import numpy as np

larray = np.linspace(1, 3, num = 3)

v1 = larray[0]**3
v2 = larray[1]**3
v3 = larray[2]**3
v = larray**3

print "Вычисление объёма вручную (поэлементно):"
print "V1 = %d, V2 = %d, V3 = %d\n" %(v1, v2, v3)

print "Вычисление объёма через умножение массива: "
print v
