import json

class JSONStorage:
    """
    A helper class for persistent storage using JSON files.
    """

    @staticmethod
    def save_to_file(data, file_path):
        with open(file_path, 'w') as f:
            json.dump(data, f)

    @staticmethod
    def load_from_file(file_path):
        try:
            with open(file_path, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return {}
