from abc import ABC, abstractmethod

class CellphoneFactoryInterface(ABC):
    """ 
    Cellphone factory interface

    This abstract class defines the interface for creating cellphone properties.

    Methods:
        create_contact(): Abstract method for creating a Contact.
        create_application(): Abstract method for creating an Application.
     
    """

    @abstractmethod
    def create_contact(self):
        """ Abstract method for creating a Contact. """
        pass

    @abstractmethod
    def create_application(self):
        """ Abstract method for creating an Application. """
        pass

    