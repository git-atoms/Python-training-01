a = int(input("a: "))
b = int(input("b: "))

# Muszą być spełnione obydwa warunki (koniunkcja)
if (a == 5 and b == 2):
    print("tak")
else:
    print("nie")


# Musi być spełniony co najmniej jeden warunek (alternatywa)
if (a == 5 or b == 2):
    print("tak")
else:
    print("nie")