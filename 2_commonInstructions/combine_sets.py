# -*- coding: utf-8 -*-

alphabet = 3
numbers = 10
cardValue = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
cardSuit = ['C', 'D', 'H', 'S']


def generateLetter(letterCount, curIndex, curStr, typeList): #type: 0 - список букв для авто, 1 - спиок мастей, 2 - список достоинств карт
    
    for j in range(0, alphabet):
        if curIndex == 0:
            for i in range(0, len(curStr)):
                curStr[i] = 0
        curStr[curIndex] = j                    
        if(letterCount != curIndex + 1):             
            generateLetter(letterCount, curIndex + 1, curStr)
        else:
            print curStr
            
letterCount = 2
numberCount = 0
curStr = []
for i in range(0, letterCount + numberCount):
    curStr.append(0)
generateLetter(letterCount, 0, curStr)