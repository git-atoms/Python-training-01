# Trzymanie LMB z opcją regulacji szybkości klikania

from pynput import keyboard
from pynput.mouse import Controller, Button
import threading
import time

class MouseControllerSimulator:
    def __init__(self):
        self.mouse_controller = Controller()
        self.clicking = False
        self.holding = False
        self.click_rate = 0  # 0 oznacza trzymanie, inne wartości to liczba kliknięć na sekundę
        self.click_rates = [10, 100, 1500, 3000]  # Dostępne szybkości kliknięć
        self.current_rate_index = -1  # -1 oznacza trzymanie, a nie klikanie
        self.thread = None

    def toggle_clicking(self):
        if not self.clicking:
            self.clicking = True
            self.thread = threading.Thread(target=self.perform_clicking)
            self.thread.start()
        else:
            self.clicking = False
            if self.thread and self.thread.is_alive():
                self.thread.join()

    def perform_clicking(self):
        if self.click_rate == 0:
            self.mouse_controller.press(Button.left)
            self.holding = True
            while self.clicking and self.holding:
                time.sleep(0.1)
            self.mouse_controller.release(Button.left)
        else:
            while self.clicking and not self.holding:
                self.mouse_controller.click(Button.left)
                time.sleep(1 / self.click_rate)

    def change_click_rate(self, direction):
        if direction == 'up':
            self.holding = False
            self.current_rate_index = max(0, self.current_rate_index)
        elif direction == 'down':
            if self.current_rate_index <= 0:
                self.holding = True
                self.current_rate_index = -1
            else:
                self.current_rate_index -= 1
        elif direction == 'right':
            self.holding = False
            self.current_rate_index = min(self.current_rate_index + 1, len(self.click_rates) - 1)
        elif direction == 'left':
            if self.current_rate_index <= 0:
                self.holding = True
                self.current_rate_index = -1
            else:
                self.current_rate_index -= 1

        if self.current_rate_index >= 0:
            self.click_rate = self.click_rates[self.current_rate_index]
        else:
            self.click_rate = 0

def on_press(key):
    try:
        if key.char == 'f':
            mouse_controller_simulator.toggle_clicking()
    except AttributeError:
        pass

    if key == keyboard.Key.up:
        mouse_controller_simulator.change_click_rate('up')
    elif key == keyboard.Key.down:
        mouse_controller_simulator.change_click_rate('down')
    elif key == keyboard.Key.right:
        mouse_controller_simulator.change_click_rate('right')
    elif key == keyboard.Key.left:
        mouse_controller_simulator.change_click_rate('left')

mouse_controller_simulator = MouseControllerSimulator()

# Nasłuchiwanie naciśnięcia klawiszy
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
