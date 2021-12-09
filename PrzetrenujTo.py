# wynik = 0

x = int(input("Podaj liczbę całkowitą: "))

if x != int:
    print("Miała być liczba całkowita, a nie ułamek")
else:
    if x >= 0:
        print(x)
    else:
        print(abs(x))