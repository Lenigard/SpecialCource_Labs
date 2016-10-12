# -*- coding: utf-8 -*-

from random import randint as rand

size = 4
numbers = []

for i in range(0, size):
    numbers.append(rand(0, 9))

print numbers