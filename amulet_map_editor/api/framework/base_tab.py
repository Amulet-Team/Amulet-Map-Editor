class BaseTab:
    def enable(self):
        """Run when the tab is shown/enabled"""
        pass

    def can_disable(self) -> bool:
        """
        Check if it is safe to disable the tab.
        :return: True if the tab can be disabled, False otherwise.
        """
        return True

    def disable(self):
        """Run when the tab is hidden/disabled"""
        pass

    def can_close(self) -> bool:
        """
        Check if it is safe to close the tab.
        If this is going to return False it should notify the user.
        :return: True if the tab can be closed, False otherwise.
        """
        return True

    def close(self):
        """Fully close the tab. Called when destroying the tab."""
        pass
