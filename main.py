from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from screens.home import HomeScreen
from screens.config import ConfigScreen
from utils.configmanager import ConfigurationManager
from utils.eventbinder import EventBinder
# Other imports...

class MainApp(App):
    def build(self):
        self.config_manager = ConfigurationManager()
        self.event_binder = EventBinder()
        self.screen_manager = ScreenManager()

        # Initialize your screens here
        home_screen = HomeScreen(name='homepage')
        config_screen = ConfigScreen(name='configuration')

        # Bind events using EventBinder
        self.event_binder.bind(home_screen)
        self.event_binder.bind(config_screen)

        # Add screens to the ScreenManager
        self.screen_manager.add_widget(home_screen)
        self.screen_manager.add_widget(config_screen)

        # Continue with other screens and utils setup...
        
        return self.screen_manager

if __name__ == '__main__':
    MainApp().run()
