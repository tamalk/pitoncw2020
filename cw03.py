# -*- coding: utf-8 -*-
r = int(input())
g = int(input())
b = int(input())
if (r >= 0) and (r <= 100) and (g >= 0) and (g <= 100) and (b >= 0) and (b <= 100):
    if r > g and r > b:
        print("El color se aproxima al rojo.")
    elif g > r and g > b:
        print("El color se aproxima al verde.")
    elif b > r and b > g:
        print("El color se aproxima al azul.")
    elif b == r and g < r:
        print("El color se aproxima al cian.")
    elif b == g and r < g:
        print("El color se aproxima al magenta.")
    elif g == r and b < g:
        print("El color se aproxima al amarillo.")
    elif g == r and g == b and g != 100 and g != 0:
        print("El color se aproxima al gris.")
    elif (r + g + b) == 0:
        print("El color es negro.")
    else:
        print("El color es blanco.")
