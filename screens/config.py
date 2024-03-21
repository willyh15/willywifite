from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.spinner import Spinner
from kivy.uix.switch import Switch
from kivy.uix.textinput import TextInput

# Import utility classes
from utils.configmanager import ConfigManager
from utils.persistence import Persistence
from utils.errorhandler import ErrorHandler

class ConfigScreen(Screen):
    def __init__(self, **kwargs):
        super(ConfigScreen, self).__init__(**kwargs)
        self.config_manager = ConfigManager()
        self.persistence = Persistence()
        self.error_handler = ErrorHandler()
        self.build()

    def build(self):
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Interface Selection
        layout.add_widget(Label(text='Wireless Interface:'))
        self.interface_spinner = Spinner(values=self.config_manager.get_interface_options())
        layout.add_widget(self.interface_spinner)

        # Attack Timeout
        layout.add_widget(Label(text='Attack Timeout (seconds):'))
        self.timeout_input = TextInput(text=str(self.config_manager.get_attack_timeout()), input_filter='int')
        layout.add_widget(self.timeout_input)

        # Advanced Options - Example: MAC Address Randomization
        layout.add_widget(Label(text='MAC Address Randomization:'))
        self.mac_switch = Switch(active=self.config_manager.get_mac_randomization_status())
        layout.add_widget(self.mac_switch)

        # Save Button
        save_btn = Button(text='Save Settings')
        save_btn.bind(on_press=self.on_save_press)
        layout.add_widget(save_btn)

        # Back Button
        back_btn = Button(text='Back')
        back_btn.bind(on_press=lambda x: self.manager.current = 'homepage')
        layout.add_widget(back_btn)

        self.add_widget(layout)

    def on_save_press(self, instance):
        # Use the error handler to manage save settings exceptions
        self.error_handler.handle(self.save_settings, instance)

    def save_settings(self, instance):
        # Update configuration manager with new settings
        self.config_manager.set_interface(self.interface_spinner.text)
        self.config_manager.set_attack_timeout(int(self.timeout_input.text))
        self.config_manager.set_mac_randomization_status(self.mac_switch.active)

        # Persist settings using the persistence utility class
        if self.persistence.save(self.config_manager.get_all_settings()):
            print("Settings saved successfully.")
        else:
            print("Failed to save settings.")
