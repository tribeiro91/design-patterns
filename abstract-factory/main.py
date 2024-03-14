from src.enums.cellphone_brands import cellphone_brands

def select_cellphone_factory(cellphone_brand):
    """Method for instancialize the factory according the cellphone brand entered into input function."""

    factory = cellphone_brands.get(cellphone_brand)
    if factory is None:
        raise ValueError("Invalid brand name.")

    return factory

def install_application(factory):
    """Method for installing an application to the cellphone according to the brand"""

    application_cellphone = factory.create_application()
    application_cellphone.install()

def main():
    """Main method where is set the cellphone brand to initialize the operation."""
    cellphone_brand = input("Enter the cellphone brand (Samsung or Motorola): ")

    cellphone_factory = select_cellphone_factory(cellphone_brand)
    install_application(cellphone_factory)


if __name__ == "__main__":
    main()