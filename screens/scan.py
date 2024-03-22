from kivy.uix.screenmanager import Screen
from kivy.uix.listview import ListView
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.adapters.listadapter import ListAdapter
from controllers.NetworkContoller import NetworkController
from services.NetworkScanService import NetworkScanService
from utils.datacarrier import DataCarrier
from utils.contentupdater import ContentUpdater
from utils.background import BackgroundTaskRunner
from utils.errorhandler import ErrorHandler

class ScanNetworksScreen(Screen):
    def __init__(self, **kwargs):
        super(ScanNetworksScreen, self).__init__(**kwargs)
        self.content_updater = ContentUpdater()
        self.data_carrier = DataCarrier()
        self.background_process = BackgroundTaskRunner()
        self.error_handler = ErrorHandler()
        self.network_controller = NetworkController(NetworkScanService())

        layout = BoxLayout(orientation='vertical')
        
        # Setup the ListView with a placeholder for network data
        self.networks_data = self.data_carrier.retrieve_data() or []
        self.list_adapter = ListAdapter(data=self.networks_data,
                                        cls=Button,
                                        args_converter=lambda row_index, rec: {'text': rec['text'],
                                                                                'size_hint_y': None,
                                                                                'height': 40})

        # The ListView widget
        self.networks_list = ListView(adapter=self.list_adapter)
        
        # Refresh and Back Buttons
        button_layout = BoxLayout(size_hint_y=None, height=50)
        refresh_btn = Button(text='Refresh', size_hint_x=None, width=100)
        back_btn = Button(text='Back', size_hint_x=None, width=100)
        refresh_btn.bind(on_press=self.on_refresh_press)  # Bind the press event to the method
        back_btn.bind(on_press=lambda x: self.manager.current = 'homepage')
        
        button_layout.add_widget(refresh_btn)
        button_layout.add_widget(back_btn)
        
        # Adding components to the layout
        layout.add_widget(self.networks_list)
        layout.add_widget(button_layout)
        
        self.add_widget(layout)

    def start_scan(self):
        results = self.network_controller.perform_scan()

    def on_refresh_press(self, instance):
        # Use the error handler to manage scanning process exceptions
        self.error_handler.handle(self.refresh_networks, instance)

    def refresh_networks(self, instance):
        # Start the network scanning in a background thread/process
        self.background_process.run(self.perform_scan, instance.text)

    def perform_scan(self, instance):
        # Placeholder for the actual scanning logic
        print(f"Scanning for networks...")
        # Here you would have the actual logic to scan the networks
        # For example, you could call a method that uses a library or system command to perform the scan

    def update_network_list(self, new_data):
        # Update the list view with new scan results using the content updater
        self.content_updater.update(self.networks_list, new_data)
