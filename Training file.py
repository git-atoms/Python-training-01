cenaNetto = float(input("Podaj cenę netto: ").replace(',','.'))
VAT = float(input("Podaj stawkę VAT: ").replace(',','.'))

obliczonyVAT = 1 + VAT/100
cenaBrutto = str(cenaNetto * obliczonyVAT).replace('.',',')

print("Cena brutto: ", cenaBrutto)