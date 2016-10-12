# -*- coding: utf-8 -*-

def average(size):
    sum = 0.
    for i in range(1, size + 1):
        sum += i
    return sum / size
    
size = input(u"Введите число, до которого нужно посчитать среднее значение: ")

print "Среднее значение суммы целых чисел от 1 до {} = {}".format(size, average(size))