# -*- coding: utf-8 -*-

a = input(u'Введите целое число a: ')   #с клавиатуры вводятся два числа а и b
b = input(u'Введите целое число b: ')

if a < b:                               #числа сравниваются
    print 'a - наименьшее из двух чисел'
elif a == b:                            #выводятся соответствующие результаты сравнения
    print 'a и b равны'
else:
    print 'b - наименьшее из двух чисел'