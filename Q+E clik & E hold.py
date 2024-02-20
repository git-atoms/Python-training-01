"""
Skrypt potrafi klikać szybko klawiszami Q + E oraz trzymać E.
Informuje także w swoim okienku czy dana opcja jest włączona czy wyłączona

"""

from pynput import keyboard
import threading
import time

# Stany aktywności funkcji
holding_e = False
clicking_qe = False

# Kontroler klawiatury
keyboard_controller = keyboard.Controller()

def hold_e():
    global holding_e
    print("Hold E: ON")
    while holding_e:
        keyboard_controller.press('e')
        time.sleep(0.01)  # Małe opóźnienie dla stabilności
    keyboard_controller.release('e')
    print("Hold E: OFF")

def click_qe():
    global clicking_qe
    print("Click Q+E: ON")
    while clicking_qe:
        keyboard_controller.press('q')
        keyboard_controller.release('q')
        time.sleep(0.01)  # Prędkość klikania
        keyboard_controller.press('e')
        keyboard_controller.release('e')
        time.sleep(0.01)  # Prędkość klikania
    print("Click Q+E: OFF")

def on_press(key):
    global holding_e, clicking_qe

    # Włącz/wyłącz trzymanie klawisza 'E' przy użyciu klawisza 'R'
    if key == keyboard.KeyCode.from_char('r'):  # Zmiana z 'e' na 'r'
        if holding_e:
            holding_e = False
        else:
            holding_e = True
            threading.Thread(target=hold_e, daemon=True).start()

    # Włącz/wyłącz sekwencyjne naciskanie 'Q' i 'E'
    if key == keyboard.KeyCode.from_char('['):
        if clicking_qe:
            clicking_qe = False
        else:
            clicking_qe = True
            threading.Thread(target=click_qe, daemon=True).start()


# Listener klawiszy
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
