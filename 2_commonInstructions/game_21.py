# -*- coding: utf-8 -*-

import random

def addCard():
    return random.randint(1,10)

takeCard = input(u"Чтобы сыграть, введите 1. Если нет, то введите 0.")
handSum = 0

while takeCard != 0:
    takeCard = input(u"Хотите взять новую карту(1/0)?")
    if takeCard == 1:
        newCard = addCard()
        print "Вы достали карту: {}".format(newCard)
        handSum += newCard
        if handSum < 22:
            print "Сумма ваших карт сейчас: {}".format(handSum)
        else:
            print "Сумма больше 21, вы проиграли!"
    else: 
        print "Ваша итоговая сумма: {}".format(handSum)
    