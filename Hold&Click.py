# 'F' klika, 'X' trzyma LMB

from pynput import keyboard
from pynput.mouse import Controller, Button
import threading
import time

class MouseActionSimulator:
    def __init__(self):
        self.mouse_controller = Controller()
        self.hold_thread = None
        self.click_thread = None
        self.holding = False
        self.clicking = False

    def toggle_hold_lmb(self):
        if self.holding:
            self.holding = False
            if self.hold_thread and self.hold_thread.is_alive():
                self.hold_thread.join()
        else:
            self.holding = True
            self.hold_thread = threading.Thread(target=self.hold_lmb)
            self.hold_thread.start()

    def hold_lmb(self):
        self.mouse_controller.press(Button.left)
        while self.holding:
            time.sleep(0.1)
        self.mouse_controller.release(Button.left)

    def toggle_click_lmb(self):
        if self.clicking:
            self.clicking = False
            if self.click_thread and self.click_thread.is_alive():
                self.click_thread.join()
        else:
            self.clicking = True
            self.click_thread = threading.Thread(target=self.click_lmb)
            self.click_thread.start()

    def click_lmb(self):
        clicks_per_second = 1500
        interval = 1.0 / clicks_per_second
        while self.clicking:
            self.mouse_controller.click(Button.left)
            time.sleep(interval)

def on_press(key):
    try:
        if key.char == 'x':
            mouse_action_simulator.toggle_hold_lmb()
        elif key.char == 'f':
            mouse_action_simulator.toggle_click_lmb()
    except AttributeError:
        pass

mouse_action_simulator = MouseActionSimulator()

# Nasłuchiwanie naciśnięcia klawiszy
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
