from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window

class HomePage(BoxLayout):
    def __init__(self, **kwargs):
        super(HomePage, self).__init__(**kwargs)
        self.orientation = 'vertical'
        
        # Adjust the window size for demonstration purposes
        Window.size = (400, 600)

        # Quick Actions Section
        actions_layout = GridLayout(cols=1, size_hint_y=None)
        actions_layout.bind(minimum_height=actions_layout.setter('height'))
        actions_layout.add_widget(Button(text='Scan Networks', size_hint_y=None, height=40))
        actions_layout.add_widget(Button(text='Attack History', size_hint_y=None, height=40))
        actions_layout.add_widget(Button(text='Settings', size_hint_y=None, height=40))

        # Status Section
        status_layout = GridLayout(cols=2, size_hint_y=None, height=120)
        status_layout.add_widget(Label(text='Interface:', halign='right'))
        status_layout.add_widget(Label(text='wlan0'))
        status_layout.add_widget(Label(text='Mode:', halign='right'))
        status_layout.add_widget(Label(text='Monitor'))
        status_layout.add_widget(Label(text='Recent:', halign='right'))
        status_layout.add_widget(Label(text='Deauth Attack'))

        # Quick Tips Section
        tips_text = ('Quick Tips:\n'
                     '- Ensure your interface is in monitor mode for scans.\n'
                     '- Use the settings to configure default attack parameters.')
        tips_layout = ScrollView(size_hint=(1, None), height=200)
        tips_content = Label(text=tips_text, size_hint_y=None)
        tips_content.bind(width=lambda *x: tips_content.setter('text_size')(tips_content, (tips_content.width, None)),
                          texture_size=lambda *x: setattr(tips_content, 'height', tips_content.texture_size[1]))
        tips_layout.add_widget(tips_content)

        # Add sections to the main layout
        self.add_widget(actions_layout)
        self.add_widget(status_layout)
        self.add_widget(tips_layout)