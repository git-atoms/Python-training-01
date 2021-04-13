# trenuję proste polecenia
# wiek = 25
# print(wiek)

'''
a = 5
b = 3
print(a+b)
'''

cenaNetto = float(input("Podaj cenę netto: "))
VAT = float(input("Podaj stawkę VAT: "))

obliczonyVAT = (1 + VAT/100)
cenaBrutto = cenaNetto * obliczonyVAT

print("Cena brutto: ", (cenaBrutto))