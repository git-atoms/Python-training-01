"""
X - trzyma LMB
F - klika LMB (1500)
C - trzyma RMB

Przy czym głównym zagadnieniem tutaj jest aby zaemulowanie LMB nie zatrzymywało włączonego RMB (i na odwrót)

"""


from pynput import keyboard
from pynput.mouse import Controller, Button
import threading
import time


class MouseActionSimulator:
    def __init__(self):
        self.mouse_controller = Controller()
        self.hold_lmb_thread = None
        self.hold_rmb_thread = None
        self.click_thread = None
        self.holding_lmb = False
        self.holding_rmb = False
        self.clicking = False

    def toggle_hold_lmb(self):
        if self.holding_lmb:
            self.holding_lmb = False
            if self.hold_lmb_thread and self.hold_lmb_thread.is_alive():
                self.hold_lmb_thread.join()
            print("LMB Hold: OFF")
        else:
            self.holding_lmb = True
            self.hold_lmb_thread = threading.Thread(target=self.hold_lmb, daemon=True)
            self.hold_lmb_thread.start()
            print("LMB Hold: ON")

    def hold_lmb(self):
        self.mouse_controller.press(Button.left)
        while self.holding_lmb:
            time.sleep(0.01)
        self.mouse_controller.release(Button.left)

    def toggle_hold_rmb(self):
        if self.holding_rmb:
            self.holding_rmb = False
            if self.hold_rmb_thread and self.hold_rmb_thread.is_alive():
                self.hold_rmb_thread.join()
            print("RMB Hold: OFF")
        else:
            self.holding_rmb = True
            self.hold_rmb_thread = threading.Thread(target=self.hold_rmb, daemon=True)
            self.hold_rmb_thread.start()
            print("RMB Hold: ON")

    def hold_rmb(self):
        self.mouse_controller.press(Button.right)
        while self.holding_rmb:
            time.sleep(0.01)
        self.mouse_controller.release(Button.right)

    def toggle_click_lmb(self):
        if self.clicking:
            self.clicking = False
            if self.click_thread and self.click_thread.is_alive():
                self.click_thread.join()
            print("LMB Click: OFF")
        else:
            self.clicking = True
            self.click_thread = threading.Thread(target=self.click_lmb, daemon=True)
            self.click_thread.start()
            print("LMB Click: ON")

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
        elif key.char == 'c':
            mouse_action_simulator.toggle_hold_rmb()
    except AttributeError:
        pass


mouse_action_simulator = MouseActionSimulator()

# Nasłuchiwanie naciśnięcia klawiszy
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
