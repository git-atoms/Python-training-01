''' Sumuje cztery wartości: zarówno dodatnie, jak i ujemne '''


wynik = 0

# "i" przechowuje przy każdym przejściu kolejny, bieżący element

for i in range (0, 4):  # w nawiasie są argumenty: zaczyna od wartości 0 powtarza działanie 4 razy
    x = int(input("Podaj wartość: "))
    wynik += x # działanie w tej pętli to dodawanie
    # print(i) #tu miała być suma pośrednia ale nieprawidłowo to wyświetlał, np. podałem wartość 1, a on wyświetlał 0
print("Wynik to: ", wynik)