wybor = input("1 dodawanie\n2 odejmowanie\n3 mnożenie\n4 dzielenie\n")
if (wybor < '1' or wybor > '4'):
    print("Wybierasz tylko to co jest w menu")

elif (wybor == '1'):
    a = int(input("Podaj pierwszą wartość: "))
    b = int(input("Podaj drugą wartość: "))
    print(str(a + b))

elif (wybor == '2'):
    a = int(input("Podaj pierwszą wartość: "))
    b = int(input("Podaj drugą wartość: "))
    print(str(a - b))

elif (wybor == '3'):
    a = int(input("Podaj pierwszą wartość: "))
    b = int(input("Podaj drugą wartość: "))
    print(str(a * b))

elif (wybor == '4'):
    a = int(input("Podaj pierwszą wartość: "))
    b = int(input("Podaj drugą wartość: "))
    if b!=0:
        print(str(a / b))
    else:
        print("Nie dzielimy przez zero")
