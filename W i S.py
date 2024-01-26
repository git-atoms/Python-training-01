# 2 sekundy ruch do przodu, 2 sekundy ruch do tyłu

from pynput import keyboard
from pynput.keyboard import Key, Controller as KeyboardController
import threading
import time

class WSKeySimulator:
    def __init__(self):
        self.active = False
        self.keyboard_controller = KeyboardController()
        self.thread = None

    def toggle_simulation(self):
        if not self.active:
            self.active = True
            self.thread = threading.Thread(target=self.simulate_ws_press)
            self.thread.start()
        else:
            self.active = False
            if self.thread:
                self.thread.join()

    def simulate_ws_press(self):
        while self.active:
            self.keyboard_controller.press('w')  # Wciśnięcie klawisza 'W'
            time.sleep(2)  # Trzymanie klawisza 'W' przez 2 sekundy
            self.keyboard_controller.release('w')  # Zwolnienie klawisza 'W'

            if not self.active:
                break  # Przerwanie pętli, jeśli akcja została zatrzymana

            self.keyboard_controller.press('s')  # Wciśnięcie klawisza 'S'
            time.sleep(2)  # Trzymanie klawisza 'S' przez 2 sekundy
            self.keyboard_controller.release('s')  # Zwolnienie klawisza 'S'

def on_press(key):
    if key == Key.f8:
        ws_key_simulator.toggle_simulation()

ws_key_simulator = WSKeySimulator()

# Nasłuchiwanie naciśnięcia klawiszy
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
