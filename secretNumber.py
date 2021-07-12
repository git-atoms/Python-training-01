''' Jeden gracz podaje jakąkolwiek wartość całkowitą, a drugi próbuje zgadnąć.
Jeśli będzie za dużo albo za mało to gracz jest o tym informowany.
Gra twa, dopóki nie padnie sekretna wartość.
'''

sekretnaLiczba = int(input("Podaj sekretną liczbę: "))
zgadywanie = 0

while zgadywanie != sekretnaLiczba:
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