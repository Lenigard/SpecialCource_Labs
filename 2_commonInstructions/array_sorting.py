# -*- coding: utf-8 -*-

from random import uniform

x = []
for i in range(0, 10):
    x.append(uniform(0, 10))
print "Первоначальный массив: "
print x

x.sort()

print "Отсортированный массив: "
print x