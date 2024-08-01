import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
from helloworld.forms.introform import Introform
from helloworld.forms.login1form import Login1form
from helloworld.forms.inputform import Inputform
from helloworld.forms.managerform import Managerform  # Assuming you have a managerform.py

class MainApp(toga.App):
    def startup(self):
        self.main_window = toga.MainWindow(title=self.formal_name)

        # Initialize forms
        self.forms = {
            "introform": Introform(self),
            "login1form": Login1form(self),
            "inputform": Inputform(self),
            "managerform": Managerform(self)
        }

        # Set the initial form to be displayed
        self.main_window.content = self.forms["introform"]
        self.main_window.show()

    def switch_form(self, form_name):
        if form_name in self.forms:
            print(f"Switching to {form_name}")
            self.main_window.content = self.forms[form_name]
        else:
            print(f"Form '{form_name}' not found")

def main():
    return MainApp('Form Switcher', 'org.beeware.formswitcher')

if __name__ == '__main__':
    main().main_loop()
