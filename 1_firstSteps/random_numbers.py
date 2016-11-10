# -*- coding: utf-8 -*-

from random import uniform as rand

size = 4
numbers = []

for i in range(0, size):
    numbers.append(rand(0, 10))

print numbers