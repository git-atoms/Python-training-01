from datetime import date
todays_date = date.today()

print ("Cześć, jestem Python, miło mi Cię poznać.\n")
imie = input("A Ty jak masz na imię?: ")
print(imie, "to ładne imię.\n")
age = input( "Ile masz lat?: ")

print("To urodziłeś się w", (todays_date.year - int(age)), "roku, prawda?")