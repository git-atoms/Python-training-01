# trenuję proste polecenia
# wiek = 25
# print(wiek)

'''
a = 5
b = 3
print(a+b)
'''

#VAT = input("Podaj stawkę VAT ")
VAT = float(input("Podaj stawkę VAT "))

# VAT = 19
obliczonyVAT = (1 + VAT/100)

cenaNettoJava = 11
cenaNettoAjax = 19

cenaBruttoJava = cenaNettoJava * obliczonyVAT
cenaBruttoAjax = cenaNettoAjax * obliczonyVAT

print("Cena brutto: ", (cenaBruttoAjax))