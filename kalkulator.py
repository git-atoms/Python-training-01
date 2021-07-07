print("Witaj w kalkulatorze.")
yn = input("Czy chcesz przejść dalej? [t/n]")

a = int(input("Pierwsza wartość: "))
b = int(input("Druga wartość: "))

if (yn == 't'):
    print("No to zaczynamy!")
    if (yn == 't'):
        choice = input("Wybierz rodzaj działania: '*'mnożenie '/'dzielenie '+'dodawanie '-'odejmowanie")
        if (choice == '*'):
            print(a*b)
        elif (choice == '/'):
            print(a/b)
        elif (choice == '+'):
            print(a+b)
        elif (choice == '-'):
            print(a-b)

elif (yn == 'n'):
    print("Do widzenia.")