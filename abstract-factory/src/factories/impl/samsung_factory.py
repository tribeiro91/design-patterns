from ..interfaces.cellphone_factory_interface import CellphoneFactoryInterface
from .samsung_contact import SamsungContact
from .samsung_application import SamsungApplication

class SamsungFactory(CellphoneFactoryInterface):
    """
    Concrete Factory for Samsung

    This concrete factory class implements the CellphoneFactoryInterface interface 
    to create the cellphone objects for Samsung cellphone.

    Attributes:
        None

    Methods:
    - create_contact(): Creates a Samsung contact object.
    - create_appication(): Creates a Samsung application object.
    """

    def create_contact(self):
        """Creates a Samsung contact object."""
        return SamsungContact()
    
    def create_application(self):
        """Creates a Samsung application object."""
        return SamsungApplication()