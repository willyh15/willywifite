from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

from utils.configmanager import ConfigurationManager
from utils.eventbinder import EventBinder
from utils.errorhandler import ErrorHandler
from utils.background import BackgroundProcess

class NetworkDetailsScreen(Screen):
    def __init__(self, network_info, **kwargs):
        super(NetworkDetailsScreen, self).__init__(**kwargs)
        self.network_info = network_info
        
        self.config_manager = ConfigurationManager()
        self.event_binder = EventBinder()
        self.error_handler = ErrorHandler()
        self.background_process = BackgroundProcess()

        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Display network details
        self.create_network_details_section(layout)

        # Create attack options section
        self.create_attack_options_section(layout)

        # Back Button
        back_btn = Button(text='Back', size_hint_y=None, height=50)
        back_btn.bind(on_press=lambda x: self.manager.current = 'scan_networks')
        layout.add_widget(back_btn)
        
        self.add_widget(layout)

    def create_network_details_section(self, layout):
        # Displaying network details
        for key, value in self.network_info.items():
            layout.add_widget(Label(text=f"{key}: {value}"))

    def create_attack_options_section(self, layout):
        # Attack Options
        attack_layout = BoxLayout(size_hint_y=None, height=50)
        for attack in ['WEP Crack', 'WPA Handshake Capture', 'Deauth Attack']:
            btn = Button(text=attack)
            btn.bind(on_press=self.initiate_attack)
            attack_layout.add_widget(btn)
        layout.add_widget(attack_layout)

    def initiate_attack(self, instance):
        # Use error handling when initiating attacks
        attack_name = instance.text
        self.error_handler.handle(self.background_process.run, self.perform_attack, attack_name, on_error=self.on_attack_error)

    def perform_attack(self, attack_name):
        # Actual attack initiation logic
        print(f"Performing {attack_name}")
        # Here you would have the actual logic for the attacks

    def on_attack_error(self, error):
        # Handle attack errors (e.g., show an error message to the user)
        print(f"Error during attack: {error}")

