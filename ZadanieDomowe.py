wynik = 0
i = 0

while i < 3:
    x = int(input("Podaj wartość parzystą: "))
    if x %2 == 0:
        wynik += x
    else:
        print("Miała być parzysta. Zapytam ponownie.")
        continue
    i += 1

print("Wynik dodania trzech wartości parzystych to: ", wynik)