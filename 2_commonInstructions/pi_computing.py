# -*- coding: utf-8 -*-

import math 
import matplotlib.pyplot as plt


def piLeib(n):
    result = 0
    for i in range(0, n):
        result += 1. / (4 * i + 1) / (4 * i + 3)
    return 8 * result
   
def piEil(n):
    result = 0
    for i in range(1, n + 1):
        result += 1. / math.pow(i, 2)
    return math.sqrt(6*result)
    

n = input(u"Введи количество разбиений для нахождения точности вычисления: ")
correctPi = math.pi
eulFault = []
leibFault = []

for i in range (1, n):
    eulFault.append(math.fabs(piEil(i) - correctPi))
    leibFault.append(math.fabs(piLeib(i) - correctPi))
    
plt.ylabel(u'Fault')
plt.xlabel(u'Number of iterations, n')
plt.title('Fault depended on number of iterations')  
plt.plot(leibFault, label = "Leibniz method")
plt.plot(eulFault, label = "Euler method")
plt.legend()
