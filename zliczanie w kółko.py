from typing import Counter


wynik = 0
i = 0

while i < 3:
    x = int(input("Podaj wartość dodatnią: "))
    if x < 0:
        print("Zliczam tylko dodatnie. Podaj właściwą wartość.")
    else:
        wynik +=x
        i+=1
        print("Sub-wynik: ",wynik)
        continue
print("Wynik dodawania to:", wynik)