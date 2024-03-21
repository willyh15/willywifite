from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

# Importing utility classes
from utils.configmanager import ConfigurationManager
from utils.eventbinder import EventBinder
from utils.errorhandler import ErrorHandler
from utils.background import BackgroundProcess

class NetworkDetailsScreen(Screen):
    def __init__(self, network_info, **kwargs):
        super(NetworkDetailsScreen, self).__init__(**kwargs)
        self.network_info = network_info  # Assuming this is a dict with network details
        
        self.config_manager = ConfigurationManager()
        self.event_binder = EventBinder()
        self.error_handler = ErrorHandler()
        self.background_process = BackgroundProcess()

        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Displaying network details
        for key, value in self.network_info.items():
            layout.add_widget(Label(text=f"{key}: {value}"))

        # Attack Options
        attack_layout = BoxLayout(size_hint_y=None, height=50)
        for attack in ['WEP Crack', 'WPA Handshake Capture', 'Deauth Attack']:
            btn = Button(text=attack)
            self.event_binder.bind_button_click(btn, self.initiate_attack)
            attack_layout.add_widget(btn)

        # Back Button
        back_btn = Button(text='Back', size_hint_y=None, height=50)
        back_btn.bind(on_press=lambda x: self.manager.current = 'scan_networks')

        layout.add_widget(attack_layout)
        layout.add_widget(back_btn)
        
        self.add_widget(layout)

    def initiate_attack(self, instance):
        # Use error handling when initiating attacks
        self.error_handler.handle(self._initiate_attack, instance)

    def _initiate_attack(self, instance):
        # Actual attack initiation logic, run in a background process
        self.background_process.run(self.perform_attack, instance.text)

    def perform_attack(self, attack_name):
        # Placeholder for attack logic
        print(f"Performing {attack_name}")
        # Here you would have the actual logic for the attacks
