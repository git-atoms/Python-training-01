print("Witaj w kalkulatorze.")
yn = input("Czy chcesz przejść dalej? [t/n]")

if (yn == 'n'):
    exit("Do widzenia.")
elif (yn == 't'):
    print("No to zaczynamy!")

print("")
choice = input("Wybierz rodzaj działania: \n * mnożenie\n / dzielenie\n + dodawanie\n - odejmowanie\n ")

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
