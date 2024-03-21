class ContentUpdater:
    """
    A helper class to dynamically update content in a Kivy application.
    """

    @staticmethod
    def update_label_text(label, new_text):
        """
        Update the text of a Label widget.
        :param label: The Label instance.
        :param new_text: The new text to set.
        """
        label.text = new_text
