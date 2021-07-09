print("Witaj w kalkulatorze.")
yn = input("Czy chcesz przejść dalej? [t/n]")

if (yn == 'n'):
    exit("Do widzenia.")
elif (yn == 't'):
    print("No to zaczynamy!")

choice = input("Wybierz rodzaj działania: \n * mnożenie\n / dzielenie\n + dodawanie\n - odejmowanie\n ")

a = float(input("Pierwsza wartość: ").replace(',','.'))
b = float(input("Druga wartość: ").replace(',','.'))

if (choice == '*'):
    print(str(a*b).replace('.',','))
elif (choice == '/'):
    if (b == 0):
        print("Nie dzielimy przez zero!")
    else:
        print(str(a/b).replace('.',','))
elif (choice == '+'):
    print(str(a+b).replace('.',','))
elif (choice == '-'):
    print(str(a-b).replace('.',','))
