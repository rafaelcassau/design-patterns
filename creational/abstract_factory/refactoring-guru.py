from random import randint

"""
Abstract Factory is a creational design pattern 
that lets you produce families of related objects
without specifying their concrete classes
"""

# buttons

class ButtonInterface:
    """
    This is the common interface for buttons family.
    """

    def paint(self):
        raise NotImplementedError


class MacOSButton(ButtonInterface):

    def paint(self):
        print('You have created MacOSButton.')


class WindowsButton(ButtonInterface):

    def paint(self):
        print('You have created WindowsButton.')


# checkboxes

class CheckboxInterface:
    """
    This is the common interface for checkbox family.
    """

    def paint(self):
        raise NotImplementedError


class MacOSCheckbox(CheckboxInterface):

    def paint(self):
        print('You have created MacOSCheckbox.')


class WindowsCheckbox(CheckboxInterface):

    def paint(self):
        print('You have created WindowsCheckbox.')


# factories

class GUIFactoryInterface:
    """
    Abstract factory knows aboult all (abstract) product types.
    """

    def create_button(self):
        raise NotImplementedError

    def create_checkbox(self):
        raise NotImplementedError


class MacOSFactory(GUIFactoryInterface):

    def create_button(self):
        return MacOSButton()

    def create_checkbox(self):
        return MacOSCheckbox()


class WindowsFactory(GUIFactoryInterface):

    def create_button(self):
        return WindowsButton()

    def create_checkbox(self):
        return WindowsCheckbox()


# application class

class Application:

    def __init__(self, factory):
        self.button = factory.create_button()
        self.checkbox = factory.create_checkbox()

    def paint(self):
        self.button.paint()
        self.checkbox.paint()


# client

class Demo:

    def configure_application(self):
        number = randint(1, 10)
        if number % 2 == 0:
            factory = MacOSFactory()
            app = Application(factory)
        else:
            factory = WindowsFactory()
            app = Application(factory)

        return app

    def run(self):
        application = self.configure_application()
        application.paint()


# run
Demo().run()
