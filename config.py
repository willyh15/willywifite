from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.switch import Switch
from kivy.uix.label import Label
from kivy.uix.spinner import Spinner
from configmanager import ConfigurationManager

configuration_schema = {
    "verbose": {"type": "boolean", "default": False},
    "interface": {"type": "choice", "choices": ["wlan0", "wlan1"], "default": "wlan0"},
    # Add more settings as needed
}

class ConfigApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        for setting, props in configuration_schema.items():
            if props['type'] == 'boolean':
                switch = Switch(active=ConfigurationManager.get(setting, props['default']))
                switch.bind(active=lambda instance, value: self.on_setting_change(setting, value))
                layout.add_widget(Label(text=setting.capitalize()))
                layout.add_widget(switch)
            elif props['type'] == 'choice':
                spinner = Spinner(
                    text=ConfigurationManager.get(setting, props['default']),
                    values=props['choices']
                )
                spinner.bind(text=lambda spinner, text: self.on_setting_change(setting, text))
                layout.add_widget(Label(text=setting.capitalize()))
                layout.add_widget(spinner)
        return layout

    def on_setting_change(self, setting, value):
        ConfigurationManager.set(setting, value)

if __name__ == '__main__':
    ConfigApp().run()
