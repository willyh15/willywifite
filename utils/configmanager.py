import json
from screens.config import configuration_schema

class ConfigurationManager:
    def __init__(self, config_path="config.json"):
        self.config_path = config_path
        self.settings = self.load_config()

    def load_config(self):
        try:
            with open(self.config_path, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return {}  # Return an empty dict if no config file is found

    def save_config(self):
        with open(self.config_path, 'w') as file:
            json.dump(self.settings, file, indent=4)

    def get(self, key, default=None):
        return self.settings.get(key, default)

    def set(self, key, value):
        # Example validation step
        prop = configuration_schema.get(key)
        if prop:
            if prop['type'] == 'boolean' and isinstance(value, bool):
                self.settings[key] = value
                self.save_config()
            elif prop['type'] == 'choice' and value in prop['choices']:
                self.settings[key] = value
                self.save_config()
            # Add more validations as necessary
        else:
            print(f"Invalid setting: {key}")