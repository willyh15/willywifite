# main.py
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from screens.home_screen import HomeScreen
from screens.scan_networks_screen import ScanNetworksScreen
from controllers.home_controller import HomeController
from controllers.network_controller import NetworkController

class MyApp(App):
    def build(self):
        # Controllers
        home_controller = HomeController()
        network_controller = NetworkController()

        # Screen Manager
        screen_manager = ScreenManager()

        # Screens
        home_screen = HomeScreen(name='home', controller=home_controller)
        scan_screen = ScanNetworksScreen(name='scan', controller=network_controller)

        # Adding screens to ScreenManager
        screen_manager.add_widget(home_screen)
        screen_manager.add_widget(scan_screen)

        return screen_manager

if __name__ == '__main__':
    MyApp().run()