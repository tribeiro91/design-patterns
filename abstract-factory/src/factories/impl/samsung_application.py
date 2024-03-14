from ..interfaces.samsung_application_interface import SamsungApplicationInterface

class SamsungApplication(SamsungApplicationInterface):
    """
    Samsung application

    This concrete class implements SamsungApplicationInterface interface 
    to create a Samsung application operations.

    Methods:
        - install(): Method for creating the ***install** operation.
        - uninstall(): Method for creating the **uninstall** operation.
        - open(): Method for creating the **open** operation.
        - close(): Method for creating the **close** operation.
    """

    def install(self):
        """Method for creating the ***install** operation."""
        print("Application has been installed.")

    def uninstall(self):
        """Method for creating the **uninstall** operation."""
        print("Application has been uninstalled.")

    def open(self):
        """Method for creating the **open** operation."""
        print("Application has been opened.")

    def close(self):
        """Method for creating the **close** operation."""
        print("Application has been closed.")