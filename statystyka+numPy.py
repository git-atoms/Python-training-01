import numpy as np

zbior_parzysty = [5,6,7,8]
zbior_nieparzysty = [5,7,8]

#obliczanie średniej arytmetycznej
srednia_arytmetyczna = np.mean(zbior_nieparzysty) #np.mean([5,7,8])
print("Średnia arytmetyczna:", srednia_arytmetyczna)


#znajdowanie mediany w rozkładzie z NIEparzystą liczbą elementów
mediana_nieparzysta = np.median(zbior_nieparzysty)
print("Mediana nieparzysta:", mediana_nieparzysta)

#znajdowanie mediany w rozkładzie z parzystą liczbą elementów
mediana_parzysta = np.median(zbior_parzysty)
print("Mediana parzysta:", mediana_parzysta)


#w numPy obliczy medianę
x = int(input("Podaj percentyl (25,50,75): "))
percentyl = np.percentile(zbior_parzysty, x) #np.percentile(a, q) gdzie 'a' to nasz zbiór (parzysty/nieparzysty), a 'q' to który percentyl (25,50,75)
print("Dla percentyla", x, "wartość mediany wynosi: ", percentyl)
"""
Przy naszym zbiorze parzystym:
#1 perc25 = (średnia arytmetyczna środka + 5) /2
#2 perc75 = (średnia arytmetyczna środka + 8) /2
# perc50 = mediana

"""
