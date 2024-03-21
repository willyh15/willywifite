from threading import Thread

class BackgroundTaskRunner:
    """
    A helper class to run background tasks in a Kivy application.
    """

    @staticmethod
    def run_in_background(target, args=(), kwargs={}):
        """
        Run a function in the background using a separate thread.
        :param target: The function to run in the background.
        :param args: The positional arguments to pass to the function.
        :param kwargs: The keyword arguments to pass to the function.
        """
        thread = Thread(target=target, args=args, kwargs=kwargs)
        thread.daemon = True
        thread.start()
