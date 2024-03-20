from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class NetworkDetailsScreen(Screen):
    def __init__(self, network_info, **kwargs):
        super(NetworkDetailsScreen, self).__init__(**kwargs)
        self.network_info = network_info  # Assuming this is a dict with network details
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Displaying network details
        for key, value in self.network_info.items():
            layout.add_widget(Label(text=f"{key}: {value}"))

        # Attack Options
        attack_layout = BoxLayout(size_hint_y=None, height=50)
        for attack in ['WEP Crack', 'WPA Handshake Capture', 'Deauth Attack']:
            btn = Button(text=attack)
            btn.bind(on_press=self.initiate_attack)
            attack_layout.add_widget(btn)

        # Back Button
        back_btn = Button(text='Back', size_hint_y=None, height=50)
        back_btn.bind(on_press=lambda x: self.manager.current = 'scan_networks')

        layout.add_widget(attack_layout)
        layout.add_widget(back_btn)
        
        self.add_widget(layout)

    def initiate_attack(self, instance):
        # Placeholder for initiating attacks
        # You might want to use the text of the instance to determine which attack to perform
        print(f"Initiating {instance.text}")
