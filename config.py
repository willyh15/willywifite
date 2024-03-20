from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.switch import Switch
from kivy.uix.label import Label

class ConfigApp(App):
    def build(self):
        self.config_manager = ConfigurationManager()
        layout = BoxLayout(orientation='horizontal')
        verbose_switch = Switch(active=self.config_manager.get('verbose', False))
        verbose_switch.bind(active=self.on_verbose_toggle)
        layout.add_widget(Label(text='Verbose'))
        layout.add_widget(verbose_switch)
        return layout

    def on_verbose_toggle(self, instance, value):
        self.config_manager.set('verbose', value)

if __name__ == '__main__':
    ConfigApp().run()
