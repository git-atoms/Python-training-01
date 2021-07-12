wynik = 0


# "i" przechowuje przy każdym przejściu kolejny, bieżący element

for i in range (0, 4):  # w nawiasie są argumenty
    x = int(input("Podaj wartość: "))
    wynik += x
    print(i)
print("Wynik to: ", wynik)