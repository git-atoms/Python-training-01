cenaNetto = float(input("Podaj cenę netto: "))
VAT = float(input("Podaj stawkę VAT: "))

obliczonyVAT = (1 + VAT/100)
cenaBrutto = cenaNetto * obliczonyVAT

print("Cena brutto: ", (cenaBrutto))