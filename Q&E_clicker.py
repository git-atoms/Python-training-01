"""
Skrypt ma klikać na zmianę klawiszami Q i E. Żadna interakcja tego nie przerywa, dopiero ponowne wciśnięcie
triggera powoduje zaprzestanie pracy skryptu.

"""

from pynput.keyboard import Controller, Listener, KeyCode
import threading
import time

class Clicker(threading.Thread):
    def __init__(self, button1, button2, delay):
        super().__init__()
        self.button1 = button1
        self.button2 = button2
        self.delay = delay
        self.running = False
        self.program_running = True

    def start_clicking(self):
        self.running = True

    def stop_clicking(self):
        self.running = False

    def exit(self):
        self.stop_clicking()
        self.program_running = False

    def run(self):
        while self.program_running:
            while self.running:
                keyboard.press(self.button1)
                keyboard.release(self.button1)
                time.sleep(self.delay)
                keyboard.press(self.button2)
                keyboard.release(self.button2)
                time.sleep(self.delay)

keyboard = Controller()
click_thread = Clicker('q', 'e', 0.01)  # 100 clicks per second
click_thread.start()

def on_press(key):
    if key == KeyCode(char='['):
        if click_thread.running:
            click_thread.stop_clicking()
        else:
            click_thread.start_clicking()

def on_release(key):
    if key == KeyCode(char='['):
        pass  # Allow the '[' key to toggle clicking on and off

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
