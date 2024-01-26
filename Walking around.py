# Idealny ruch po okręgu (chodzenie dookoła)

from pynput import keyboard
from pynput.keyboard import Key, Controller
import threading
import time

class CircleMovementSimulator:
    def __init__(self):
        self.active = False
        self.keyboard_controller = Controller()
        self.thread = None

    def start_movement(self):
        if not self.active:
            self.active = True
            if self.thread is None or not self.thread.is_alive():
                self.thread = threading.Thread(target=self.move_in_circle)
                self.thread.start()

    def stop_movement(self):
        self.active = False
        if self.thread and self.thread.is_alive():
            self.thread.join()

    def move_in_circle(self):
        self.keyboard_controller.press('w')  # Rozpoczęcie ruchu po okręgu od razu
        while self.active:
            self.keyboard_controller.press('d')  # Rozpoczęcie skrętu w prawo
            time.sleep(1.5)  # Trzymanie klawisza 'D' przez 1,5 sekundy
            self.keyboard_controller.release('d')  # Zakończenie skrętu
            if not self.active:
                break  # Natychmiastowe zatrzymanie, jeśli akcja została dezaktywowana

        self.keyboard_controller.release('w')
        self.keyboard_controller.release('d')

def on_press(key):
    if key == keyboard.KeyCode.from_char('g'):
        if circle_movement_simulator.active:
            circle_movement_simulator.stop_movement()
        else:
            circle_movement_simulator.start_movement()

circle_movement_simulator = CircleMovementSimulator()

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
