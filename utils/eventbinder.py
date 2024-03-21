class EventBinder:
    """
    A helper class to manage event bindings in a Kivy application.
    """

    @staticmethod
    def bind_button_to_action(button, action, *args, **kwargs):
        """
        Bind a button to a specific action (method).
        :param button: The button instance to bind the action to.
        :param action: The action (method) to be called when the button is pressed.
        :param args: Additional positional arguments to pass to the action.
        :param kwargs: Additional keyword arguments to pass to the action.
        """
        button.bind(on_press=lambda instance: action(*args, **kwargs))
