wybor = input("1 dodawanie\n2 odejmowanie\n3 mnożenie\n4 dzielenie\n")
a = int(input("Podaj pierwszą wartość: "))
b = int(input("Podaj drugą wartość: "))

if (wybor == '1'):
    print(str(a+b))

elif (wybor == '2'):
    print(a-b)

elif (wybor == '3'):
    print(str(a*b))

elif (wybor == '4'):
    if b!=0:
        print(str(a / b))
    else:
        print("Nie dzielimy przez zero")
