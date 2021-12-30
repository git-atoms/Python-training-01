"""
1. User podaje swoją sekretną wartość.
2. Drugi user próbuje ją zgadnąć.
3. Program sprawdza czy podana wartość to nasza sekretna.
"""
tryAgain = "Spróbuj jeszcze raz."
confirm = "Tak, sekretna liczba to:"
gratz = "Gratuluję!"

sekret = int(input("Witaj. Podaj sekretną liczbę: "))
i = 0

while i != sekret:
    x = int(input("Zgadnij sekretną liczbę: "))
    if x > sekret:
        print("Za dużo.")
        continue
    elif x < sekret:
        print("Za mało.")
        continue
    else:
        print(confirm, sekret)
        break