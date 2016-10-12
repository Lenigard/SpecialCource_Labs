# -*- coding: utf-8 -*-

                    # Привет - SyntaxError: invalid syntax

v0 = 5       # Начальная скорость

                    # При удалении знака комментария - SyntaxError: invalid syntax
                    # При удалении = - SyntaxError: invalid syntax

g = 9.81            # Ускорение свободного падения
t = 0.6             # Время

y = v0*t - 0.5*g*t**2
                    # y = v0*t - y = 3.0
                    # y = v0*t - (1/2)*g*t**2 - y = 3.0
                    
print y             # При pint - SyntaxError: invalid syntax
                    # При print x - NameError: name 'x' is not defined

