class DataCarrier:
    """
    A helper class to pass data between screens.
    """
    data_store = {}

    @classmethod
    def store_data(cls, key, value):
        """
        Store data with a specific key.
        :param key: The key for the data.
        :param value: The value to store.
        """
        cls.data_store[key] = value

    @classmethod
    def retrieve_data(cls, key, default=None):
        """
        Retrieve data with a specific key.
        :param key: The key for the data.
        :param default: The default value if key is not found.
        """
        return cls.data_store.get(key, default)
