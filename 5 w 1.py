"""
Z - chodzi
C - trzyma RMB
X - trzyma LMB
F - klika szybko LMB
F8 - scroll down (odsuwa ekran)
G - chodzi w kółko (musi być widok od góry)
[ - klika szybko Q i E
R - trzyma E

O tym czy dana opcja jest włączona (ON) czy wyłączona (OFF) informuje w swoim okienku

"""

from pynput import keyboard
from pynput.mouse import Button, Controller as MouseController
from pynput.keyboard import Controller as KeyboardController
import threading
import time

# Kontrolery
mouse_controller = MouseController()
keyboard_controller = KeyboardController()

# Stany aktywności
states = {
    'walk': False,
    'rmb': False,
    'lmb': False,
    'clicking': False,
    'scrolling': False,
    'walking_circle': False,
    'clicking_qe': False,
    'holding_e': False
}

def toggle_state(state_key):
    states[state_key] = not states[state_key]
    print(f"{state_key.upper()}: {'ON' if states[state_key] else 'OFF'}")

def perform_action():
    while True:
        if states['walk']:
            keyboard_controller.press('w')
            time.sleep(0.1)
            keyboard_controller.release('w')

        if states['rmb']:
            mouse_controller.press(Button.right)
        else:
            mouse_controller.release(Button.right)

        if states['lmb']:
            mouse_controller.press(Button.left)
        else:
            mouse_controller.release(Button.left)

        if states['clicking']:
            mouse_controller.click(Button.left)
            time.sleep(0.1)

        if states['scrolling']:
            mouse_controller.scroll(0, -2)
            time.sleep(0.1)

        if states['walking_circle']:
            for key in ['w', 'd', 's', 'a']:
                keyboard_controller.press(key)
                time.sleep(1)
                keyboard_controller.release(key)

        if states['clicking_qe']:
            keyboard_controller.press('q')
            keyboard_controller.release('q')
            keyboard_controller.press('e')
            keyboard_controller.release('e')
            time.sleep(0.1)

        if states['holding_e']:
            keyboard_controller.press('e')
        else:
            keyboard_controller.release('e')

        time.sleep(0.1)

def on_press(key):
    try:
        if key.char == 'z':
            toggle_state('walk')
        elif key.char == 'c':
            toggle_state('rmb')
        elif key.char == 'x':
            toggle_state('lmb')
        elif key.char == 'f':
            toggle_state('clicking')
        elif key.char == 'r':
            toggle_state('holding_e')
    except AttributeError:
        if key == keyboard.Key.f8:
            toggle_state('scrolling')
        elif key == keyboard.KeyCode.from_char('g'):
            toggle_state('walking_circle')
        elif key == keyboard.KeyCode.from_char('['):
            toggle_state('clicking_qe')

# Uruchomienie wątku działania
threading.Thread(target=perform_action, daemon=True).start()

# Nasłuchiwacz naciśnięć klawiszy
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
