from abc import ABC, abstractmethod

class SamsungContactInterface(ABC):
    """
    Samsung contact interface

    This abstract class defines the interface for creating a Samsung contact operations.

    Methods:
        - create(): Abstract method for creating the creating operation.
        - update(): Abstract method for creating the update operation.
        - delete(): Abstract method for creating the delete operation.
        - call(): Abstract method for creating the calling operation.
        - send_text_message(): Abstract method for creating the sending of text message operation.
    """

    @abstractmethod
    def create(self):
        """Abstract method for creating the creating operation."""
        pass

    @abstractmethod
    def update(self):
        """Abstract method for creating the update operation."""
        pass

    @abstractmethod
    def delete(self):
        """Abstract method for creating the delete operation."""
        pass

    @abstractmethod
    def call(self):
        """Abstract method for creating the calling operation."""
        pass

    @abstractmethod
    def send_text_message(self):
        """Abstract method for creating the sending of text message operation."""
        pass
