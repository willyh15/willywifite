from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.spinner import Spinner
from kivy.uix.switch import Switch
from kivy.uix.textinput import TextInput

configuration_schema = {
    "verbose": {"type": "boolean", "default": False},
    "interface": {"type": "choice", "choices": ["wlan0", "wlan1"], "default": "wlan0"},
    # Add more settings as needed
}

class ConfigScreen(Screen):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Interface Selection
        layout.add_widget(Label(text='Wireless Interface:'))
        self.interface_spinner = Spinner(values=('wlan0', 'wlan1'))  # Example values
        layout.add_widget(self.interface_spinner)

        # Attack Timeout
        layout.add_widget(Label(text='Attack Timeout (seconds):'))
        self.timeout_input = TextInput(text='60', input_filter='int')
        layout.add_widget(self.timeout_input)

        # Advanced Options - Example: MAC Address Randomization
        layout.add_widget(Label(text='MAC Address Randomization:'))
        self.mac_switch = Switch(active=True)
        layout.add_widget(self.mac_switch)

        # Save Button
        save_btn = Button(text='Save Settings')
        save_btn.bind(on_press=self.save_settings)
        layout.add_widget(save_btn)

        # Back Button
        back_btn = Button(text='Back')
        back_btn.bind(on_press=lambda x: self.manager.current = 'homepage')
        layout.add_widget(back_btn)

        self.add_widget(layout)

    def save_settings(self, instance):
        # Logic to save the settings
        # You would typically update your configuration manager here
        print(f"Interface: {self.interface_spinner.text}, Timeout: {self.timeout_input.text}, MAC Randomization: {'Enabled' if self.mac_switch.active else 'Disabled'}")