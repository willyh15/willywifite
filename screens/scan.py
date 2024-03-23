from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.adapters.listadapter import ListAdapter
from kivy.uix.listview import ListView

from controllers.network_controller import NetworkController
from services.network_scan_service import NetworkScanService
from utils.errorhandler import ErrorHandler
from utils.background import BackgroundProcess

class ScanNetworksScreen(Screen):
    def __init__(self, **kwargs):
        super(ScanNetworksScreen, self).__init__(**kwargs)
        self.network_controller = NetworkController(NetworkScanService())
        self.error_handler = ErrorHandler()
        self.background_process = BackgroundProcess()

        layout = BoxLayout(orientation='vertical')
        
        # Initially, networks_data will be empty or loaded from a saved state
        self.networks_data = []

        # Setup for ListView
        self.list_adapter = ListAdapter(
            data=self.networks_data,
            cls=Button,
            args_converter=lambda row_index, rec: {'text': rec['text'],
                                                   'size_hint_y': None,
                                                   'height': 40}
        )
        self.networks_list = ListView(adapter=self.list_adapter)
        
        # UI setup for Refresh and Back Buttons
        button_layout = BoxLayout(size_hint_y=None, height=50)
        refresh_btn = Button(text='Refresh', size_hint_x=None, width=100)
        back_btn = Button(text='Back', size_hint_x=None, width=100)

        refresh_btn.bind(on_press=self.on_refresh_press)
        back_btn.bind(on_press=lambda x: self.manager.current = 'homepage')
        
        button_layout.add_widget(refresh_btn)
        button_layout.add_widget(back_btn)
        
        layout.add_widget(self.networks_list)
        layout.add_widget(button_layout)
        
        self.add_widget(layout)

    def on_refresh_press(self, instance):
        # Handle the refresh action with error handling and a background process
        self.error_handler.handle(self.background_process.run, self.perform_scan, on_error=self.on_scan_error)

    def perform_scan(self):
        # Call perform_scan from NetworkController in the background
        new_data = self.network_controller.perform_scan()
        # Schedule the update on the main thread since it modifies the UI
        self.dispatch('on_update', new_data)

    def on_scan_error(self, error):
        # Handle scan errors (e.g., show an error message to the user)
        pass

    def on_update(self, *args):
        # Triggered when new scan data is ready to be displayed
        new_data = args[1]
        self.update_network_list(new_data)

    def update_network_list(self, new_data):
        # Update the ListView with new data
        self.list_adapter.data = new_data
        self.networks_list._trigger_reset_populate()

ScanNetworksScreen.register_event_type('on_update')