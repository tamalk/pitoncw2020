# -*- coding: utf-8 -*-
year = int(input())
cent = year + 100
current = 2020
left = cent - current
if (year > 2019):
    print("¡No ha habido ninguna innovacion en esta fecha!")
elif (year < 1939):
    print("En esa fecha HP todavia no existia.")
else:
    print("En " + str(left) + " años se producira un centenario.")
