from ..interfaces.cellphone_factory_interface import CellphoneFactoryInterface
from .motorola_application import MotorolaApplication
from .motorola_contact import MotorolaContact

class MotorolaFactory(CellphoneFactoryInterface):
    """
    Concrete Factory for Motorola

    This concrete factory class implements the CellphoneFactoryInterface interface 
    to create the cellphone objects for Motorola cellphone.

    Attributes:
        None

    Methods:
    - create_contact(): Creates a Motorola contact object.
    - create_appication(): Creates a Motorola application object.
    """

    def create_contact(self):
        """Creates a Motorola contact object."""
        return MotorolaContact()
    
    def create_application(self):
        """Creates a Motorola application object."""
        return MotorolaApplication()