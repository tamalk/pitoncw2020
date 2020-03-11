inp = str(input())
inp2 = inp.upper()
defstring = "El color se aproxima al "
red, green, blue = 0, 0, 0
for i in range(len(inp2)):
    if inp2[i] == "R":
        red += 1
    elif inp2[i] == "G":
        green += 1
    elif inp2[i] == "B":
        blue += 1
if red > green and red > blue:
    print(defstring + " rojo")
elif green > red and green > blue:
    print(defstring + " verde")
elif blue > red and blue > green:
    print(defstring + " azul")
elif green == blue and red < green:
    print(defstring + " magenta")
elif green == red and blue < red:
    print(defstring + " amarillo")
elif blue == red and green < red:
    print(defsting + " morado")
elif green == red and green == blue:
    print("El color es negro")
