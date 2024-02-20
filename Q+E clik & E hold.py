"""
Skrypt potrafi klikać szybko klawiszami Q + E oraz trzymać E.
Informuje także w swoim okienku czy dana opcja jest włączona czy wyłączona

"""

from pynput.keyboard import Key, Listener, KeyCode
from pynput.mouse import Button, Controller as MouseController
import threading
import time

class Clicker(threading.Thread):
    def __init__(self):
        super().__init__(daemon=True)
        self.running = False
        self.program_running = True
        self.holding_e = False

    def start_clicking(self):
        self.running = True

    def stop_clicking(self):
        self.running = False

    def start_holding_e(self):
        self.holding_e = True
        print("Trzymanie 'E': ON")

    def stop_holding_e(self):
        self.holding_e = False
        print("Trzymanie 'E': OFF")

    def exit(self):
        self.stop_clicking()
        self.stop_holding_e()
        self.program_running = False

    def run(self):
        while self.program_running:
            while self.running:
                mouse.click(Button.left)
                time.sleep(0.01)  # 100 clicks per second
            if self.holding_e:
                keyboard.press('e')
            else:
                keyboard.release('e')
            time.sleep(0.1)

mouse = MouseController()
keyboard = Controller()
click_thread = Clicker()
click_thread.start()

def on_press(key):
    if key == KeyCode(char='['):
        if click_thread.running:
            click_thread.stop_clicking()
            print("Klikanie 'Q+E': OFF")
        else:
            click_thread.start_clicking()
            print("Klikanie 'Q+E': ON")
    elif key == Key.ctrl and key == KeyCode(char='e'):
        if click_thread.holding_e:
            click_thread.stop_holding_e()
        else:
            click_thread.start_holding_e()

def on_release(key):
    pass

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
