from ..factories.impl.motorola_factory import MotorolaFactory
from ..factories.impl.samsung_factory import SamsungFactory

cellphone_brands = {
    "Motorola" : MotorolaFactory(),
    "Samsung": SamsungFactory()
}