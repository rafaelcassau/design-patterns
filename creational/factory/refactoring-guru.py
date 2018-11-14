from random import randint


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
        # Create and render a Windows looking button.
        print("TKInter (Test Button)")
        self.on_click()

    def on_click(self):
        # Bind a native OS click event.
        print("WINDOWS -> Button says - 'Hello World!'")


class HTMLButton(ButtonInterface):

    def render(self):
        # Return an HTML representation of a button.
        print("<button>Test Button</button>")
        self.on_click()

    def on_click(self):
        # Bind a web browser click event.
        print("HTML -> Click! Button says - 'Hello World!'")


class AbstractDialog:
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


class WindowsDialog(AbstractDialog):
    """
    Concrete factories extend that method to produce different
    kinds of products.
    """
    def create_button(self):
        return WindowsButton()


class WebDialog(AbstractDialog):
    """
    Concrete factories extend that method to produce different
    kinds of products.
    """
    def create_button(self):
        return HTMLButton()


class ClientApplication:

    def __init__(self):
        self.configure()

    def configure(self):
        number = randint(1, 10)
        if number % 2 == 0:
            self.dialog = WindowsDialog()
        else:
            self.dialog = WebDialog()

    def run_business_logic(self):
        self.dialog.render_window()


# run
ClientApplication().run_business_logic()
