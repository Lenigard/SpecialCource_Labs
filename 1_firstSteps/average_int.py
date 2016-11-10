# -*- coding: utf-8 -*-
size = 5
correct_value = 3

sum = 0.
for i in range(1, size + 1):
    sum += i

print "Полученный результат = {}".format(sum / size);
print "Погрешность вычисления (разность между правильным и полученным значениями): {}".format(sum / size - correct_value)