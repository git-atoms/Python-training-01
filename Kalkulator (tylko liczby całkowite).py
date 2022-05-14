from traceback import print_tb


print("\n Kalkulator liczb całkowitych")
wybor = input("1 dodawanie\n2 odejmowanie\n3 mnożenie\n4 dzielenie\n")

# Walidacja menu wyboru (można wybrać tylko pomiędzy 1, a 4
#  Nie przechodzi testu, kiedy dokonamy więcej niż jednego wyboru i oddzielimy je przecinkami np. "2,3"
if (wybor < '1' or wybor > '4'):
    print("Wybierasz tylko to co jest w menu")

# Dodawanie
elif (wybor == '1'):
    a = int(input("Podaj pierwszą wartość: "))
    b = int(input("Podaj drugą wartość: "))
    print(str(a + b))

# Odejmowanie
elif (wybor == '2'):
    a = int(input("Podaj pierwszą wartość: "))
    b = int(input("Podaj drugą wartość: "))
    print(str(a - b))

# Mnożenie
elif (wybor == '3'):
    a = int(input("Podaj pierwszą wartość: "))
    b = int(input("Podaj drugą wartość: "))
    print(str(a * b))

# Dzielenie (nie dzieli przez ułamki)
elif (wybor == '4'):
    a = int(input("Podaj pierwszą wartość: "))
    b = int(input("Podaj drugą wartość: "))
    
# Walidacja dzielenia przez zero    
    if b!=0:
        print(str(a / b))
    else:
        print("Nie dzielimy przez zero")

input("Wciśnij ENTER, żeby zakończyć")
exit()