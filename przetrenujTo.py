suma = 0
i = 0 #ilość wykonanych cykli pętli
while i < 5:

    x = int(input("Podaj wartość: "))
    suma +=x
    i += 1
    print("Wynik tymczasowy to:", suma)

print("Łączny wynik tego dodawania to:", suma)