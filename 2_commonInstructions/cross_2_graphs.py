# -*- coding: utf-8 -*-

from math import fabs

def xCreate(x, n):
    num = -4.
    delta = 8./n
    for i in range(0, n + 1):
        x.append(num)
        num += delta
    return x
    
def pointCheck(x, epsilon):
    for i in range(0, len(x)):
        f = x[i]
        g = x[i]**2
        if fabs(f - g) <= epsilon:
            print "Точка верная"
        else: 
            print "Точка неверная" 

varepsilon = input(u"Введите погрешность: ")
n = input(u"Введите количество разбиений: ")

x = []
xCreate(x, n)
pointCheck(x, varepsilon)