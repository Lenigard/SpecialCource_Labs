# -*- coding: utf-8 -*-

import random

genNum =[]
n = input(u"Введите количество чисел, которое будет сгенерировано: ")
for i in range(0, n):
    genNum.append(random.randint(1,6))
count = 0
for i in genNum:
    if i == 6:
        count += 1
        
print float(count)/len(genNum)       
print genNum