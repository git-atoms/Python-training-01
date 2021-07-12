''' Jeden gracz podaje jakąkolwiek wartość całkowitą, a drugi próbuje zgadnąć

'''

sekretnaLiczba = int(input("Podaj sekretną liczbę: "))
i = 0

while i != sekretnaLiczba:
    zgadywanie = int(input("Zgadnij liczbę całkowitą: "))
    if zgadywanie > sekretnaLiczba:
        print("Za dużo.")
        continue
    elif zgadywanie == sekretnaLiczba:
        print("Gratulacje, trafiona!")
        break
    else:
        print("Za mało. Próbuj dalej.")
        continue