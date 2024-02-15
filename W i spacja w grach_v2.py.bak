# Klawisz 'Q' skakanie (spacja), klawisz 'E' chodzenie do przodu ('W')

from pynput import keyboard
from pynput.keyboard import Key, Controller

class KeySimulator:
    def __init__(self):
        self.w_pressed = False
        self.space_pressed = False
        self.keyboard_controller = Controller()

    def toggle_w(self):
        if not self.w_pressed:
            self.keyboard_controller.press('w')
            self.w_pressed = True
        else:
            self.keyboard_controller.release('w')
            self.w_pressed = False

    def toggle_space(self):
        if not self.space_pressed:
            self.keyboard_controller.press(Key.space)
            self.space_pressed = True
        else:
            self.keyboard_controller.release(Key.space)
            self.space_pressed = False

def on_press(key):
    if key == keyboard.KeyCode.from_char('e'):
        key_simulator.toggle_w()
    elif key == keyboard.KeyCode.from_char('q'):
        key_simulator.toggle_space()

key_simulator = KeySimulator()

# Nasłuchiwanie naciśnięcia klawiszy
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
