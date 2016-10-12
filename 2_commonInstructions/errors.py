# -*- coding: utf-8 -*-
# Программа для вычисления положения мяча при вертикальном движении
# с использованием функции

def y(t) :
                   # при удалении ":" - SyntaxError: invalid syntax
                   # при удалении открывающей скобки - SyntaxError: invalid syntax
                    # при удалении аргумента - TypeError: y() takes no arguments (1 given)
   v0 = 5          # Начальная скорость
                    #при удалении отступа - IndentationError: expected an indented block
                    #при добавлении отступа - IndentationError: unindent does not match any outer indentation level
   g = 9.81       # Ускорение свободного падения
   return v0*t - 0.5*g*t**2
	
t = 0.6             # Время
print y(t)           #при удалении t - TypeError: y() takes exactly 1 argument (0 given)
t = 0.9
print y(t)

