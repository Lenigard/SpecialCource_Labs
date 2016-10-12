# -*- coding: utf-8 -*-

from numpy import pi

def squareCount(r):
    return pi/2*r**2
    
def perimeterCount(r):
    return 2*pi*r

r = input(u"Введите радиус окружности: ")

A = squareCount(r)
C = perimeterCount(r)

print "Периметр = {:.5}, площадь = {:.5}".format(C, A)