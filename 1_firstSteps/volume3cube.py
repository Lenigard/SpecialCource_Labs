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
print "Вычисление объёма через умножение массива: V1 = {}, V2 = {}, V3 = {}".format(v[0], v[1], v[2])
print "Погрешность вычисления (разность между правильным и полученным значениями): {}, {}, {}".format(v[0]-v1_correct, v[1]-v2_correct, v[2]-v3_correct)


plt.xlabel(u'L, length')
plt.ylabel(u'V, volume')
plt.title('Volume depended on side length')  
plt.plot(l, v)
plt.show()