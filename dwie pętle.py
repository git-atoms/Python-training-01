liczba = 0 #wartość startowa
i = 0 #ilość cykli

while liczba < 10:
    liczba +=1
    i +=1
    print(liczba)

#kiedy z górnej pętli otrzymał pierwsze dziesięć wartości, dokłada od siebie kolejne pięć (bo tyle ma w zakresie)
for i in range(0,5):
    liczba +=1
    i +=1
    print(liczba)