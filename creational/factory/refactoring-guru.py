from random import randint


# buttons

class ButtonInterface:
    """
    The Factory Method pattern is applicable only when there is a products hierarchy.
    """

    def render(self):
        raise NotImplementedError

    def on_click(self):
        raise NotImplementedError


class WindowsButton(ButtonInterface):

    def render(self):
        print("TKInter (Test Button)")
        self.on_click()

    def on_click(self):
        print("WINDOWS -> Button says - 'Hello World!'")


class HTMLButton(ButtonInterface):

    def render(self):
        print("<button>Test Button</button>")
        self.on_click()

    def on_click(self):
        print("HTML -> Click! Button says - 'Hello World!'")


# dialogs factory methods

class AbstractDialogFactoryMethod:
    """
    Base factory class. Note that the "factory" is merely a role
    for the class. It should have some core business logic which
    needs different products to be created.
    """
    def render_window(self):
        # Render other window controls.
        ok_button = self.create_button()
        ok_button.render()

    def create_button(self):
        # Therefore we extract all product creation code to a
        # special factory method.
        raise NotImplementedError


class WindowsDialogFactoryMethod(AbstractDialogFactoryMethod):
    """
    Concrete factories extend that method to produce different
    kinds of products.
    """
    def create_button(self):
        return WindowsButton()


class WebDialogFactoryMethod(AbstractDialogFactoryMethod):
    """
    Concrete factories extend that method to produce different
    kinds of products.
    """
    def create_button(self):
        return HTMLButton()


# client application

class ClientApplication:

    def __init__(self):
        self.configure()

    def configure(self):
        number = randint(1, 10)
        if number % 2 == 0:
            self.dialog = WindowsDialogFactoryMethod()
        else:
            self.dialog = WebDialogFactoryMethod()

    def run_business_logic(self):
        self.dialog.render_window()


# run
ClientApplication().run_business_logic()
