from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.slider import Slider
from kivy.clock import Clock
import threading
import requests

# === Configuration ===
MOTOR_IDS = [7, 8, 11, 12, 18, 19, 20, 30, 32]
TOKEN = "61f5b898-063b-4847-a859-dbc37b3a346d"
BASE_URL = "https://192.168.1.24/api"
HEADERS = {
    "Authorization": f"Bearer {TOKEN}",
    "accept": "application/json",
    "Content-Type": "application/json"
}

# === API Functions ===
def send_motor_command(motor_id, event_type, button_type):
    try:
        url = f"{BASE_URL}/loads/{motor_id}/ctrl/{event_type}/{button_type}"
        response = requests.get(url, headers=HEADERS, verify=False)
        print(f"Command sent to {motor_id}: {event_type}/{button_type}", response.text)
    except Exception as e:
        print("Error sending command:", e)

def set_motor_target_state(motor_id, level, tilt=0):
    try:
        payload = {"level": level, "tilt": tilt}
        url = f"{BASE_URL}/loads/{motor_id}/target_state"
        response = requests.put(url, headers=HEADERS, json=payload, verify=False)
        print(f"Set target_state for {motor_id}:", response.text)
    except Exception as e:
        print("Error setting target state:", e)

# === UI ===
class MotorControl(BoxLayout):
    def __init__(self, motor_id, **kwargs):
        super().__init__(orientation='horizontal', size_hint_y=None, height=40, **kwargs)
        self.motor_id = motor_id
        self.level = 50  # default level in percent

        self.label = Label(text=f"Motor {motor_id}", size_hint_x=0.25)
        self.add_widget(self.label)

        self.down_btn = Button(text="Down", on_press=self.move_down)
        self.up_btn = Button(text="Up", on_press=self.move_up)
        self.stop_btn = Button(text="Stop", on_press=self.stop_motor)
        self.slider = Slider(min=0, max=100, value=self.level)
        self.slider.bind(value=self.on_slider_change)
        self.set_btn = Button(text="Set %", on_press=self.set_target)

        self.add_widget(self.down_btn)
        self.add_widget(self.up_btn)
        self.add_widget(self.stop_btn)
        self.add_widget(self.slider)
        self.add_widget(self.set_btn)

    def move_up(self, instance):
        threading.Thread(target=send_motor_command, args=(self.motor_id, "press", "up")).start()

    def move_down(self, instance):
        threading.Thread(target=send_motor_command, args=(self.motor_id, "press", "down")).start()

    def stop_motor(self, instance):
        threading.Thread(target=send_motor_command, args=(self.motor_id, "press", "stop")).start()

    def set_target(self, instance):
        level_value = int(self.slider.value * 100)
        threading.Thread(target=set_motor_target_state, args=(self.motor_id, level_value)).start()

    def on_slider_change(self, instance, value):
        self.level = int(value)

class MotorApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        for motor_id in MOTOR_IDS:
            layout.add_widget(MotorControl(motor_id))
        return layout

if __name__ == '__main__':
    MotorApp().run()
