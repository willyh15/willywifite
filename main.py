from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class MainApp(App):
    def build(self):
        self.config = Configuration()  # Assuming the Configuration class is defined
        layout = BoxLayout(orientation='vertical')
        scan_btn = Button(text='Scan Networks')
        scan_btn.bind(on_press=self.scan_networks)  # Connect button press to function
        layout.add_widget(scan_btn)
        return layout

    def scan_networks(self, instance):
        interface = self.config.get_setting('interface', 'wlan0')
        networks = scan_networks(interface)  # Assuming scan_networks function is defined
        print(networks)  # Replace with updating the UI with the networks found

MainApp().run()
