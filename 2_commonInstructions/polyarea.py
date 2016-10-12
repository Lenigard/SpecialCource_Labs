# -*- coding: utf-8 -*-

import math

def distance(x, y):
    a = math.pow(x[0] - y[0], 2)
    b = math.pow(x[1] - y[1], 2)
    return math.sqrt(a + b)
def squareTriangle(d1, d2, d3):
    
    p = (d1 + d2 + d3)/2
    return math.sqrt(p * (p - d1) * (p - d2) * (p - d3))


def square(x, y):
    start = [x[0], y[0]];
    next1 = [x[1], y[1]];
    next2 = [x[2], y[2]];
    square = 0.
    d1 = distance(start, next1)
    d2 = distance(next1, next2)
    d3 = distance(next2, start)
    curNum = 2
    while curNum < len(x):
        curNum += 1
        square += squareTriangle(d1, d2, d3)
        if curNum != len(x):
            next1[0] = next2[0]
            next1[1] = next2[1]
            next2[0] = x[curNum]
            next2[1] = y[curNum]
            d1 = d3
            d2 = distance(next1, next2)
            d3 = distance(next2, start)
    return square
        
x = [0.,4., 0.]
y = [0., 1., 4.]     

# программа работает для любого многоугольника

print quare(x, y)