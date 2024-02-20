from pynput import keyboard
import threading
import time

class KeyboardActions:
    def __init__(self):
        self.holding_e = False
        self.clicking_qe = False
        self.keyboard_controller = keyboard.Controller()

    def hold_e(self):
        print("Hold E: ON")
        while self.holding_e:
            self.keyboard_controller.press('e')
            time.sleep(0.01)
        self.keyboard_controller.release('e')
        print("Hold E: OFF")

    def click_qe(self):
        print("Click Q+E: ON")
        while self.clicking_qe:
            self.keyboard_controller.press('q')
            self.keyboard_controller.release('q')
            time.sleep(0.01)
            self.keyboard_controller.press('e')
            self.keyboard_controller.release('e')
            time.sleep(0.01)
        print("Click Q+E: OFF")

    def on_press(self, key):
        if key == keyboard.KeyCode.from_char('r'):
            self.holding_e = not self.holding_e
            if self.holding_e:
                threading.Thread(target=self.hold_e, daemon=True).start()
            # Tutaj nie ma potrzeby zatrzymywania wątku, ponieważ jest on typu daemon.

        elif key == keyboard.KeyCode.from_char('['):
            self.clicking_qe = not self.clicking_qe
            if self.clicking_qe:
                threading.Thread(target=self.click_qe, daemon=True).start()
            # Podobnie jak wyżej, nie ma potrzeby zatrzymywania wątku typu daemon.


keyboard_actions = KeyboardActions()

with keyboard.Listener(on_press=keyboard_actions.on_press) as listener:
    listener.join()
