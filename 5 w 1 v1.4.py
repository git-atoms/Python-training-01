"""
Z - chodzi
C - trzyma RMB
X - trzyma LMB
F - klika szybko LMB (1500 klinięć na sekundę)
F7 - scroll up (przybliża ekran)
F8 - scroll down (odsuwa ekran)
G - chodzi w kółko (widok powinien być od góry inaczej będzie chodził po większym promieniu)
[ - klika szybko Q i E
R - trzyma E
T - trzyma E przez 3 sekundy, puszcza i znowu trzyma przez 3 sekundy (loop)
V - skacze (spacja)

O tym czy dana opcja jest włączona (ON) czy wyłączona (OFF) informuje w swoim okienku


"""

from pynput import keyboard
from pynput.keyboard import Controller as KeyboardController
from pynput.keyboard import Key
from pynput.mouse import Controller as MouseController
from pynput.mouse import Button
import threading
import time


# 01 - Trzymanie 'W' i spacji (ruch do przodu i skakanie)
class KeySimulator:
    def __init__(self):
        self.w_pressed = False
        self.space_pressed = False
        self.keyboard_controller = KeyboardController()

# 01a - Klawisz 'W'
    def toggle_w(self):
        if not self.w_pressed:
            self.keyboard_controller.press('w')
            self.w_pressed = True
            print("\nChodzenie: ON \n(aby wyłączyć naciśnij 'Z')")
        else:
            self.keyboard_controller.release('w')
            self.w_pressed = False
            print("Chodzenie: OFF")

# 01b - Spacja
    def toggle_space(self):
        if not self.space_pressed:
            self.keyboard_controller.press(Key.space)
            self.space_pressed = True
            print("\nSpacja: ON \n(aby wyłączyć naciśnij 'V')")
        else:
            self.keyboard_controller.release(Key.space)
            self.space_pressed = False
            print("Spacja: OFF")


# 02 - Akcje przycisków myszy
class MouseActionSimulator:
    def __init__(self):
        self.mouse_controller = MouseController()
        self.hold_lmb_thread = None
        self.hold_rmb_thread = None
        self.holding_lmb = False
        self.holding_rmb = False

# 02a - Trzymanie LMB
    def toggle_hold_lmb(self):
        self.holding_lmb = not self.holding_lmb
        if self.holding_lmb:
            self.hold_lmb_thread = threading.Thread(target=self.hold_lmb, daemon=True)
            self.hold_lmb_thread.start()
            print("\nLMB Hold: ON \n(aby wyłączyć naciśnij 'X')")
        else:
            if self.hold_lmb_thread and self.hold_lmb_thread.is_alive():
                self.hold_lmb_thread.join()
            print("LMB Hold: OFF")

    def hold_lmb(self):
        while self.holding_lmb:
            self.mouse_controller.press(Button.left)
            time.sleep(0.1)
        self.mouse_controller.release(Button.left)

# 02b - Trzymanie RMB
    def toggle_hold_rmb(self):
        self.holding_rmb = not self.holding_rmb
        if self.holding_rmb:
            self.hold_rmb_thread = threading.Thread(target=self.hold_rmb, daemon=True)
            self.hold_rmb_thread.start()
            print("\nRMB Hold: ON \n(aby wyłączyć naciśnij 'C')")
        else:
            if self.hold_rmb_thread and self.hold_rmb_thread.is_alive():
                self.hold_rmb_thread.join()
            print("RMB Hold: OFF")

    def hold_rmb(self):
        while self.holding_rmb:
            self.mouse_controller.press(Button.right)
            time.sleep(0.1)
        self.mouse_controller.release(Button.right)

# 02c - Klikanie 1500 kliknięć na sekundę
    def toggle_click_lmb(self):
        if self.clicking:
            self.clicking = False
            if self.click_thread and self.click_thread.is_alive():
                self.click_thread.join()
            print("LMB Click fast: OFF")
        else:
            self.clicking = True
            self.click_thread = threading.Thread(target=self.click_lmb, daemon=True)
            self.click_thread.start()
            print("\nLMB Click fast: ON \n(aby wyłączyć naciśnij 'F')")

    def click_lmb(self):
        clicks_per_second = 1500
        interval = 1.0 / clicks_per_second
        while self.clicking:
            self.mouse_controller.click(Button.left)
            time.sleep(interval)


# 03down - Scroll down (oddalanie ekranu)
class ScrollSimulator:
    def __init__(self):
        self.scrolling = False
        self.mouse_controller = MouseController()
        self.scroll_thread = None

    def toggle_scroll_down(self):
        self.scrolling = not self.scrolling
        if self.scrolling:
            threading.Thread(target=self.scroll_down, daemon=True).start()
            print("\nOddalenie ekranu: ON \n(aby wyłączyć naciśnij 'F8')")
        else:
            print("Oddalenie ekranu: OFF")

    def scroll_down(self):
        while self.scrolling:
            self.mouse_controller.scroll(0, -1)  # Scroll down
            time.sleep(0.1)

# 03up - Scroll up (przybliżanie ekranu)

    def toggle_scroll_up(self):
        self.scrolling = not self.scrolling
        if self.scrolling:
            threading.Thread(target=self.scroll_up, daemon=True).start()
            print("\nPrzybliżenie ekranu: ON \n(aby wyłączyć naciśnij 'F7')")
        else:
            print("Przybliżenie ekranu: OFF")

    def scroll_up(self):
        while self.scrolling:
            self.mouse_controller.scroll(0, 1)  # Scroll up
            time.sleep(0.1)


# 04 - Sekwencja chodzenia
class KeySequenceSimulator:
    def __init__(self):
        self.active = False
        self.keyboard_controller = KeyboardController()
        self.thread = None

    def toggle_simulation(self):
        if not self.active:
            self.active = True
            if self.thread is None or not self.thread.is_alive():
                self.thread = threading.Thread(target=self.simulate_key_sequence)
                self.thread.start()
                print("\nChodzenie dookoła: ON \n(aby wyłączyć naciśnij 'G')")
        else:
            print("\nChodzenie dookoła: OFF \n(zaraz przestanie chodzić)")
            self.active = False
            if self.thread and self.thread.is_alive():
                self.thread.join()

    def simulate_key_sequence(self):
        keys = ['w', 's', 'a', 'd']
        while self.active:
            for key in keys:
                time.sleep(0.1)
                if not self.active:
                    break
                self.keyboard_controller.press(key)
                if key == 'd':
                    time.sleep(5)  # Trzymanie każdego innego klawisza przez 1 sekundę
                self.keyboard_controller.release(key)


# 05 - Spamowanie Q+E oraz trzymanie E
class KeyboardActions:
    def __init__(self):
        self.holding_e = False
        self.clicking_qe = False
        self.hold_e_thread = None  # Zmienione z False na None, aby wskazywać brak wątku
        self.click_qe_thread = None  # Podobnie jak wyżej
        self.keyboard_controller = keyboard.Controller()

# 05a - Trzymanie E
    def toggle_hold_e(self):
        if self.holding_e:
            self.holding_e = False
            if self.hold_e_thread and self.hold_e_thread.is_alive():
                self.hold_e_thread.join()
            print("Trzymanie E: OFF")
        else:
            self.holding_e = True
            self.hold_e_thread = threading.Thread(target=self.hold_e, daemon=True)
            self.hold_e_thread.start()
            print("\nTrzymanie E: ON \n(aby wyłączyć naciśnij 'R')")

# To jest trzymanie klawisza 'E' wciśniętego
    def hold_e(self):
        self.keyboard_controller.press('e')  # Naciśnij 'e' na początku
        while self.holding_e:
            time.sleep(0.1)  # Utrzymuj pętlę, ale bez ciągłego naciskania 'e'
        self.keyboard_controller.release('e')  # Puść 'e', gdy self.holding_e będzie False

# 05b - Trzymanie E przez 3 sekundy (loop)
    def toggle_hold_e_loop(self):
        if self.holding_e:
            self.holding_e = False
            if self.hold_e_thread and self.hold_e_thread.is_alive():
                self.hold_e_thread.join()
            print("Pętla E: OFF")
        else:
            self.holding_e = True
            self.hold_e_thread = threading.Thread(target=self.hold_e_loop, daemon=True)
            self.hold_e_thread.start()
            print("\nPętla E: ON \n(aby wyłączyć naciśnij 'T')")

# Trzymanie klawisza 'E' wciśniętego przez 3 sekundy (loop)
    def hold_e_loop(self):
        while self.holding_e:
            self.keyboard_controller.press('e')  # Naciśnij 'e'
            time.sleep(3)  # Trzymaj 'e' przez 3 sekundy
            self.keyboard_controller.release('e')  # Puść 'e'
            if not self.holding_e:  # Sprawdź, czy pętla powinna zostać zatrzymana
                break
            time.sleep(0.1)  # Krótka przerwa przed ponownym naciśnięciem 'e'

# 05c - Spamowanie Q+E
    def toggle_click_qe(self):
        if self.clicking_qe:
            self.clicking_qe = False
            if self.click_qe_thread and self.click_qe_thread.is_alive():
                self.click_qe_thread.join()
            print("Spam Q+E: OFF")
        else:
            self.clicking_qe = True
            self.click_qe_thread = threading.Thread(target=self.click_qe, daemon=True)
            self.click_qe_thread.start()
            print("\nSpam Q+E: ON \n(aby wyłączyć naciśnij '[')")

    def click_qe(self):
        while self.clicking_qe:
            self.keyboard_controller.press('q')
            self.keyboard_controller.release('q')
            time.sleep(0.01)
            self.keyboard_controller.press('e')
            self.keyboard_controller.release('e')
            time.sleep(0.01)


key_simulator = KeySimulator()
mouse_action_simulator = MouseActionSimulator()
scroll_simulator = ScrollSimulator()
key_sequence_simulator = KeySequenceSimulator()
keyboard_actions = KeyboardActions()


def on_press(key):

    # Trzymanie W i spacji
    if key == keyboard.KeyCode.from_char('z'):
        key_simulator.toggle_w()
    elif key == keyboard.KeyCode.from_char('v'):
        key_simulator.toggle_space()

    # Akcje klawiszami myszy
    elif hasattr(key, 'char') and key.char in ['x', 'f', 'c']:
        if key.char == 'x':
            mouse_action_simulator.toggle_hold_lmb()
        elif key.char == 'f':
            mouse_action_simulator.toggle_click_lmb()
        elif key.char == 'c':
            mouse_action_simulator.toggle_hold_rmb()

    # Scroll down F8
    elif key == keyboard.Key.f8:
        scroll_simulator.toggle_scroll_down()
    
    # Scroll down F7
    elif key == keyboard.Key.f7:
        scroll_simulator.toggle_scroll_up()

    # Chodzenie
    elif key == keyboard.KeyCode.from_char('g'):
        key_sequence_simulator.toggle_simulation()

    # Trzymanie E
    elif key == keyboard.KeyCode.from_char('r'):
        keyboard_actions.toggle_hold_e()
    
    # Trzymanie E przez 3 sekundy (loop)
    elif key == keyboard.KeyCode.from_char('t'):
        keyboard_actions.toggle_hold_e_loop()

    # Spamowanie Q+E
    elif key == keyboard.KeyCode.from_char('['):
        keyboard_actions.toggle_click_qe()


# Listener for key presses
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
