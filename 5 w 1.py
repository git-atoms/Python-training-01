"""
Z - chodzi
C - trzyma RMB
X - trzyma LMB
F - klika szybko LMB
F8 - scroll down (odsuwa ekran)
G - chodzi w kółko (musi być widok od góry)
[ - klika szybko Q i E
R - trzyma E

O tym czy dana opcja jest włączona (ON) czy wyłączona (OFF) informuje w swoim okienku

"""

from pynput import keyboard
from pynput.mouse import Controller as MouseController
from pynput.keyboard import Key, Controller as KeyboardController
import threading
import time

# KeySimulator for toggling 'W' and 'Space'
class KeySimulator:
    def __init__(self):
        self.w_pressed = False
        self.space_pressed = False
        self.keyboard_controller = KeyboardController()

    def toggle_w(self):
        if not self.w_pressed:
            self.keyboard_controller.press('w')
            self.w_pressed = True
            print("W: ON")
        else:
            self.keyboard_controller.release('w')
            self.w_pressed = False
            print("W: OFF")

    def toggle_space(self):
        if not self.space_pressed:
            self.keyboard_controller.press(Key.space)
            self.space_pressed = True
            print("Space: ON")
        else:
            self.keyboard_controller.release(Key.space)
            self.space_pressed = False
            print("Space: OFF")

# MouseActionSimulator for mouse actions
class MouseActionSimulator:
    def __init__(self):
        self.mouse_controller = MouseController()
        self.holding_lmb = False
        self.holding_rmb = False
        self.clicking = False

    def toggle_hold_lmb(self):
        self.holding_lmb = not self.holding_lmb
        if self.holding_lmb:
            self.mouse_controller.press(MouseController.left)
            print("LMB Hold: ON")
        else:
            self.mouse_controller.release(MouseController.left)
            print("LMB Hold: OFF")

    def toggle_hold_rmb(self):
        self.holding_rmb = not self.holding_rmb
        if self.holding_rmb:
            self.mouse_controller.press(MouseController.right)
            print("RMB Hold: ON")
        else:
            self.mouse_controller.release(MouseController.right)
            print("RMB Hold: OFF")

    def toggle_click_lmb(self, clicks_per_second=1500):
        if not self.clicking:
            self.clicking = True
            threading.Thread(target=self.click_lmb, args=(clicks_per_second,), daemon=True).start()
        else:
            self.clicking = False

    def click_lmb(self, clicks_per_second):
        interval = 1.0 / clicks_per_second
        while self.clicking:
            self.mouse_controller.click(MouseController.left)
            time.sleep(interval)
        print("LMB Click: OFF")

# ScrollSimulator for scrolling functionality
class ScrollSimulator:
    def __init__(self):
        self.scrolling = False
        self.mouse_controller = MouseController()

    def toggle_scroll(self):
        self.scrolling = not self.scrolling
        if self.scrolling:
            threading.Thread(target=self.scroll_down, daemon=True).start()
        else:
            print("Scroll: OFF")

    def scroll_down(self):
        while self.scrolling:
            self.mouse_controller.scroll(0, -1)  # Scroll down
            time.sleep(0.1)
        print("Scroll: OFF")

# KeySequenceSimulator for simulating a sequence of key presses
class KeySequenceSimulator:
    def __init__(self):
        self.active = False
        self.keyboard_controller = KeyboardController()

    def toggle_simulation(self):
        self.active = not self.active
        if self.active:
            threading.Thread(target=self.simulate_key_sequence, daemon=True).start()
        else:
            print("Key Sequence: OFF")

    def simulate_key_sequence(self):
        keys = ['w', 's', 'a', 'd']
        while self.active:
            for key in keys:
                time.sleep(0.1)
                self.keyboard_controller.press(key)
                time.sleep(1)  # Hold each key for 1 second
                self.keyboard_controller.release(key)
        print("Key Sequence: OFF")

key_simulator = KeySimulator()
mouse_action_simulator = MouseActionSimulator()
scroll_simulator = ScrollSimulator()
key_sequence_simulator = KeySequenceSimulator()

def on_press(key):
    # Toggling 'W' and 'Space'
    if key == keyboard.KeyCode.from_char('z'):
        key_simulator.toggle_w()
    elif key == keyboard.KeyCode.from_char('v'):
        key_simulator.toggle_space()

    # Mouse actions
    elif hasattr(key, 'char') and key.char in ['x', 'f', 'c']:
        if key.char == 'x':
            mouse_action_simulator.toggle_hold_lmb()
        elif key.char == 'f':
            mouse_action_simulator.toggle_click_lmb()
        elif key.char == 'c':
            mouse_action_simulator.toggle_hold_rmb()

    # Scrolling
    elif key == keyboard.Key.f8:
        scroll_simulator.toggle_scroll()

    # Key sequence simulation
    elif key == keyboard.KeyCode.from_char('g'):
        key_sequence_simulator.toggle_simulation()

# Listener for key presses
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
