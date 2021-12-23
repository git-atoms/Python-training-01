""" Oblicza silnię """

silnia = 1
i = 1
x = int(input("Oblicz silnię z: "))
while i <= x:
    silnia *= i
    i += 1
print("Silnia z", x, "to: ", silnia)