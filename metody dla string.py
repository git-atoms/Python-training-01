"""
Metody piszemy po kropce. Dla stringa piszemy "pizza".capitalize, dla zadeklarowanej zmiennej po prostu po kropce
"""

# czysty string
print("pizza".title())


# capitalize
""" Ustawia dużą literę tylko na początku pierwszego słowa """
first_name = "clint"
last_name = "eastwood"
full_name = first_name + ", " + last_name
print(full_name.capitalize())


# title()
""" Ustawia duże litery (wszystkie pierwsze, w każdym słowie) """
first_name = "clint"
last_name = "eastwood"
full_name = first_name + ", " + last_name
print(full_name.title())


# join()
""" Łączy wszystkie elementy w iterowalnym zestawie, z naszym stringiem """
txt = "Mój numer telefonu to:"
print(txt,'-'.join(['123', '456', '789']))