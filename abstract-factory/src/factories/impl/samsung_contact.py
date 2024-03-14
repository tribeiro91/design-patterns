from ..interfaces.samsung_contact_interface import SamsungContactInterface

class SamsungContact(SamsungContactInterface):
    """
    Samsung contact class

    This concrete class implements the SamsungContactInterface interface 
    to create a Samsung contact operations.

    Methods:
        - create(): Method for creating the **create** operation.
        - update(): Method for creating the **update** operation.
        - delete(): Method for creating the **delete** operation.
        - call(): Method for creating the **call** operation.
        - send_text_message(): Method for creating the **sending of text message** operation.
    """

    def create(self):
        """Method for creating the **create** operation."""
        print("Contact has been created.")

    def update(self):
        """Method for creating the **update** operation."""
        print("Contact has been updated.")

    def delete(self):
        """Method for creating the **delete** operation."""
        print("Contact has been deleted.")

    def call(self):
        """Method for creating the **call** operation."""
        print("Calling to your friend.")

    def send_text_message(self):
        """Method for creating the **sending of text message** operation."""
        print("Message has been sent.")
