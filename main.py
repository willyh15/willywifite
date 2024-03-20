from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

# Import your configuration manager and other necessary components
from screens.home import HomeScreen
from screens.config import ConfigScreen
from screens.scan import ScanNetworksScreen
from screens.networkdetails import NetworkDetailsScreen
from utils.configmanager import ConfigurationManager
# Assuming you have other screens defined elsewhere
# from screens import SettingsScreen, OtherScreen

# You can define your screens in KV language or Python
# For simplicity, here's an example using Python

configuration_schema = {
    "verbose": {"type": "boolean", "default": False},
    "interface": {"type": "choice", "choices": ["wlan0", "wlan1"], "default": "wlan0"},
    # Add more settings as needed
}

class MainApp(App):
    def build(self):
        self.config_manager = ConfigurationManager()
        self.screen_manager = ScreenManager()
        
        self.screen_manager.add_widget(HomeScreen(name='homepage'))
        self.screen_manager.add_widget(ConfigScreen(name='configuration'))
        self.screen_manager.add_widget(ScanNetworksScreen('scan'))
        self.screen_manager.add_widget(NetworkDetailsScreen('network'))
    
        
        return self.screen_manager
    
if __name__ == '__main__':
    MainApp().run()   
