suma_parzystych = 0
i = 0

while i < 3:
    x = int(input("Podaj wartość parzystą: "))
    if x % 2 == 0:
        suma_parzystych += x
        i += 1
    else:
        print("Miały być tylko parzyste! Podaj właściwą wartość.")
        continue
print("Suma trzech wartości parzystych to:", suma_parzystych)