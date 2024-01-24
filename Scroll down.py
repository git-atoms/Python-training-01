# Scroll down: pomocny kiedy stoimy przy scianie i kamera przybliza sie do postaci zawezajac tym samym pole widzenia

from pynput import keyboard
from pynput.mouse import Controller as MouseController
import threading
import time

class ScrollSimulator:
    def __init__(self):
        self.scrolling = False
        self.mouse_controller = MouseController()
        self.scroll_thread = None

    def toggle_scroll(self):
        if not self.scrolling:
            self.scrolling = True
            self.scroll_thread = threading.Thread(target=self.scroll_down)
            self.scroll_thread.start()
        else:
            self.scrolling = False
            if self.scroll_thread:
                self.scroll_thread.join()

    def scroll_down(self):
        while self.scrolling:
            self.mouse_controller.scroll(0, -1)  # Przewijanie w dół
            time.sleep(0.1)  # Przerwa między przewijaniami

def on_press(key):
    if key == keyboard.Key.f8:
        scroll_simulator.toggle_scroll()

scroll_simulator = ScrollSimulator()

# Nasłuchiwanie naciśnięcia klawiszy
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
