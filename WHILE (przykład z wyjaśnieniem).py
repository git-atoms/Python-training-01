#Zaczynamy od zera bo jest neutralne przy dodawaniu.
wynik = 0

#Tu jest "silnik" naszej pętli.
i = 0
while i < 4:


#Tutaj są przeliczane wartości.
    x = int(input("Podaj wartość: "))
    wynik += x
    i +=1
    print("Wynik tymczasowy to:", wynik)

#A tu drukuje się wynik.
#Z racji tego, że PRINT jest bez wcięcia, będzie pokazany tylko raz, na samym końcu.
print("Łączny wynik tego dodawania to:", wynik)
