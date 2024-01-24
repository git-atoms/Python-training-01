# F8 robi scroll down (oddala widok) + "trzyma" lewy przycisk myszy (faktycznie klika nim co 0,1 sekundy)

from pynput import keyboard
from pynput.mouse import Controller as MouseController, Button
import threading
import time

class ScrollAndClickSimulator:
    def __init__(self):
        self.active = False
        self.mouse_controller = MouseController()
        self.action_thread = None

    def toggle_action(self):
        if not self.active:
            self.active = True
            self.action_thread = threading.Thread(target=self.scroll_and_click)
            self.action_thread.start()
        else:
            self.active = False
            if self.action_thread:
                self.action_thread.join()

    def scroll_and_click(self):
        while self.active:
            self.mouse_controller.scroll(0, -1)  # Przewijanie w dół
            self.mouse_controller.press(Button.left)  # Naciśnięcie lewego przycisku myszy
            time.sleep(0.05)  # Krótka przerwa
            self.mouse_controller.release(Button.left)  # Zwolnienie lewego przycisku myszy
            time.sleep(0.05)  # Przerwa między akcjami

def on_press(key):
    if key == keyboard.Key.f8:
        scroll_and_click_simulator.toggle_action()

scroll_and_click_simulator = ScrollAndClickSimulator()

# Nasłuchiwanie naciśnięcia klawiszy
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
