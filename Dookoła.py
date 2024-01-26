# Kiedy jest widok pionowy z góry
# postać chodzi dookoła

from pynput import keyboard
from pynput.keyboard import Key, Controller as KeyboardController
import threading
import time

class KeySequenceSimulator:
    def __init__(self):
        self.active = False
        self.keyboard_controller = KeyboardController()
        self.thread = None

    def toggle_simulation(self):
        if not self.active:
            self.active = True
            if self.thread is None or not self.thread.is_alive():
                self.thread = threading.Thread(target=self.simulate_key_sequence)
                self.thread.start()
        else:
            self.active = False
            if self.thread and self.thread.is_alive():
                self.thread.join()

    def simulate_key_sequence(self):
        keys = ['w', 's', 'a', 'd']
        while self.active:
            for key in keys:
                time.sleep(0.1)
                if not self.active:
                    break
                self.keyboard_controller.press(key)
                if key == 'd':
                    time.sleep(5)  # Trzymanie każdego innego klawisza przez 1 sekundę
                self.keyboard_controller.release(key)

def on_press(key):
    if key == keyboard.KeyCode.from_char('g'):
        key_sequence_simulator.toggle_simulation()

key_sequence_simulator = KeySequenceSimulator()

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
