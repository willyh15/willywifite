class ScreenManagerHelper:
    """
    A helper class to manage screen transitions in a Kivy application.
    """

    @staticmethod
    def switch_to_screen(screen_manager, screen_name):
        """
        Switches to a screen with a specific name.
        :param screen_manager: The ScreenManager instance.
        :param screen_name: The name of the screen to switch to.
        """
        if screen_manager.has_screen(screen_name):
            screen_manager.current = screen_name
        else:
            print(f"No screen with name {screen_name} found in ScreenManager.")
