n = input()
nstripped = n[: : 2]
pointsum = 0
free = 0
normal = 0
trip = 0
hasbroken = 0

for i in range(len(nstripped)):
    shot = int(nstripped[i])
    if shot > 3 or shot < 1:
        hasbroken = 1
        break
    else:
        pointsum = pointsum + shot
        if shot == 1:
            free += 1
        elif shot == 2:
            normal += 1
        else:
            trip += 1
if hasbroken != 1:
    print("Kobe Bryant ha encestado un total de " + str(pointsum) + "puntos") 
    print("Triples: " + str(trip))
    print("Tiros de campo: " + str(normal))
    print("Tiros libres: " + str(free))
else:
    print("No existen puntos con ese valor.")
