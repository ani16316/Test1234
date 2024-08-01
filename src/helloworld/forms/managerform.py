import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW, LEFT, RIGHT
from datetime import datetime

class Managerform(toga.Box):
    def __init__(self, app):
        super().__init__(style=Pack(direction=COLUMN, padding=10))
        self.app = app

        # Create input elements
        self.first_name_input = toga.TextInput(placeholder='First Name')
        self.last_name_input = toga.TextInput(placeholder='Last Name')
        self.manager_input = toga.TextInput(placeholder='Manager')
        self.site_input = toga.TextInput(placeholder='Site')
        self.training_name_input = toga.TextInput(placeholder='Training Name')
        self.date_input = toga.TextInput(placeholder='YYYY-MM-DD')
        self.date_input.on_change = self.validate_date
        self.urgency_input = toga.Selection(items=['Low', 'Medium', 'High'])

        # Create buttons
        submit_button = toga.Button('Submit', on_press=self.submit_form, style=Pack(background_color='maroon', color='white', padding=(5, 10)))
        clear_button = toga.Button('Clear', on_press=self.clear_form, style=Pack(padding=(5, 10)))

        # Create layout
        box = toga.Box(children=[
            toga.Box(children=[
                toga.Label('First Name:', style=Pack(padding=(5, 0), width=150, text_align=RIGHT)),
                self.first_name_input
            ], style=Pack(direction=ROW, padding=(5, 0))),
            toga.Box(children=[
                toga.Label('Last Name:', style=Pack(padding=(5, 0), width=150, text_align=RIGHT)),
                self.last_name_input
            ], style=Pack(direction=ROW, padding=(5, 0))),
            toga.Box(children=[
                toga.Label('Manager:', style=Pack(padding=(5, 0), width=150, text_align=RIGHT)),
                self.manager_input
            ], style=Pack(direction=ROW, padding=(5, 0))),
            toga.Box(children=[
                toga.Label('Site:', style=Pack(padding=(5, 0), width=150, text_align=RIGHT)),
                self.site_input
            ], style=Pack(direction=ROW, padding=(5, 0))),
            toga.Box(children=[
                toga.Label('Training Name:', style=Pack(padding=(5, 0), width=150, text_align=RIGHT)),
                self.training_name_input
            ], style=Pack(direction=ROW, padding=(5, 0))),
            toga.Box(children=[
                toga.Label('Date:', style=Pack(padding=(5, 0), width=150, text_align=RIGHT)),
                self.date_input
            ], style=Pack(direction=ROW, padding=(5, 0))),
            toga.Box(children=[
                toga.Label('Urgency:', style=Pack(padding=(5, 0), width=150, text_align=RIGHT)),
                self.urgency_input
            ], style=Pack(direction=ROW, padding=(5, 0))),
            toga.Box(children=[
                submit_button,
                toga.Label('', style=Pack(width=20)),
                clear_button
            ], style=Pack(direction=ROW, padding=(10, 0))),
        ], style=Pack(direction=COLUMN, padding=10))

        # Add the box to the main window
        self.add(box)

    def validate_date(self, widget):
        try:
            # Attempt to parse the date
            datetime.strptime(widget.value, '%Y-%m-%d')
            widget.style.background_color = 'white'  # Valid date
        except ValueError:
            widget.style.background_color = 'red'  # Invalid date

    def submit_form(self, widget):
        # Implement form submission logic here
        print("Form submitted")
        self.go_to_introform(widget)

    def clear_form(self, widget):
        self.first_name_input.value = ''
        self.last_name_input.value = ''
        self.manager_input.value = ''
        self.site_input.value = ''
        self.training_name_input.value = ''
        self.date_input.value = ''
        self.urgency_input.value = None

    def go_to_introform(self, widget):
        self.app.switch_form("introform")
