# -*- coding: utf-8 -*-

from numpy import linspace 
import matplotlib.pyplot as plt


l = linspace(1, 3, num = 3)

v1_correct = 1.
v2_correct = 8.
v3_correct = 27.
v = l**3

print "Вычисление объёма вручную (поэлементно):"
print "V1 = %d, V2 = %d, V3 = %d\n" %(v1_correct, v2_correct, v3_correct)

print "Вычисление объёма через умножение массива: "
print v

plt.xlabel(u'L, length')
plt.ylabel(u'V, volume')
plt.title('Volume depended on side length')  
plt.plot(l, v)