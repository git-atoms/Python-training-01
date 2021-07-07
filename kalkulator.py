print("Witaj w kalkulatorze.")
yn = input("Czy chcesz przejść dalej? [t/n]")

if (yn == 'n'):
    exit("Do widzenia.")
elif (yn == 't'):
    print("No to zaczynamy!")

print("Wybierz rodzaj działania:")
choice = input("'*'mnożenie '/'dzielenie '+'dodawanie '-'odejmowanie ")

a = int(input("Pierwsza wartość: "))
b = int(input("Druga wartość: "))

if (choice == '*'):
    print(a*b)
elif (choice == '/'):
    if (b == 0):
        print("Nie dzielimy przez zero!")
    else:
        print(a/b)
elif (choice == '+'):
    print(a+b)
elif (choice == '-'):
    print(a-b)
