a = int(input("Podaj pierwszą liczbę: "))
b = int(input("Podaj drugą liczbę: "))

if (a < b):
    print(a, "jest mniejsze od", b)
elif (b < a):
    print(a, "jest większe od", b)
else:
    print ("Obie wartości są równe.")