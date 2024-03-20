from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

# Import your configuration manager and other necessary components
from screens.home import HomePage
from screens.config import ConfigApp
from utils.configmanager import ConfigurationManager
# Assuming you have other screens defined elsewhere
# from screens import SettingsScreen, OtherScreen

# You can define your screens in KV language or Python
# For simplicity, here's an example using Python

class MainApp(App):
    def build(self):
        self.config_manager = ConfigurationManager()
        self.screen_manager = ScreenManager()
        
        # Add your homepage screen
        self.screen_manager.add_widget(HomePage(name='homepage'))
        self.screen_manager.add_widget(ConfigApp(name='configuration'))
        
        # Optionally, add other screens
        # self.screen_manager.add_widget(SettingsScreen(name='settings'))
        
        return self.screen_manager
