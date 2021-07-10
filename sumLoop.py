#do tego zera będzie dodawało 'x' czyli wartości, które podamy
wynik = 0

# do tego 'i' będzie zliczało, ile razy pętla już przeszła
i= 0
while i < 4: #wykona pętlę 4 razy, czyli 4 razy poprosi o podanie liczby i wtedy, na koniec poda wynik tego dodawania
    x = int(input("Podaj wartość: "))
    wynik += x #do wyniku dodaje kolejne 'x'
    i += 1 #po każdym przejściu pętli dodaje sobie, ile razy już przeszło; kiedy osiągnie warunek 'while' to przejdzie niżej do 'print'

print("Wynik dodawania to: ", wynik)