import tkinter as tk
import requests
import datetime

def get_atomic_time():
    try:
        response = requests.get("http://worldtimeapi.org/api/timezone/Europe/Warsaw")
        data = response.json()
        datetime_str = data['datetime']
        datetime_obj = datetime.datetime.fromisoformat(datetime_str)
        return datetime_obj.strftime('%H:%M:%S')
    except Exception as e:
        return f"Błąd: {e}"

def update_time():
    current_time = get_atomic_time()
    time_label.config(text=current_time)
    root.after(1000, update_time)  # Odświeżanie co 1 sekundę

def get_temperature():
    try:
        response = requests.get("http://ip-api.com/json/")
        data = response.json()
        lat, lon = data['lat'], data['lon']
        
        weather_response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid=c2e0c3dd58a723cb1f5ad75beb49c557&units=metric")
        weather_data = weather_response.json()
        temperature = weather_data['main']['temp']
        return temperature
    except Exception as e:
        print(f"Wystąpił błąd: {e}")
        return "Błąd"


def update_temperature():
    temperature = get_temperature()
    if temperature == "Błąd":
        temperature_label.config(text="Błąd pobierania temperatury")
    else:
        temperature_label.config(text=f"Temperatura: {temperature} °C")
    root.after(1800000, update_temperature)  # Odświeżanie co 30 minut

root = tk.Tk()
root.title("Czas i Temperatura")

# Ramka dla czasu
time_frame = tk.Frame(root)
time_frame.pack(pady=10)
time_label = tk.Label(time_frame, font=('Helvetica', 48), fg='black')
time_label.pack()
update_time()  # Rozpoczęcie aktualizacji czasu

# Ramka dla temperatury
temperature_frame = tk.Frame(root)
temperature_frame.pack(pady=10)
temperature_label = tk.Label(temperature_frame, font=('Helvetica', 24), fg='blue')
temperature_label.pack()
update_temperature()  # Rozpoczęcie aktualizacji temperatury

root.mainloop()
