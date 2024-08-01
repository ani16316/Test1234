import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW, LEFT, RIGHT

class Inputform(toga.Box):
    def __init__(self, app):
        super().__init__(style=Pack(direction=COLUMN, padding=10))
        self.app = app

        # Create input elements
        self.project_select = toga.Selection(items=['Acciona Construction South Australia', 'Project 2', 'Project 3'])
        self.contractor_select = toga.Selection(items=['All Contractors', 'Contractor 1', 'Contractor 2'])
        self.keyword_input = toga.TextInput(placeholder='Keyword')
        self.show_expired = toga.Switch('Show Expired')
        self.project_status_select = toga.Selection(items=['All Statuses', 'Status 1', 'Status 2'])
        self.onsite_checkbox = toga.Switch('Onsite')
        self.offsite_checkbox = toga.Switch('Offsite')

        # Create buttons
        filter_button = toga.Button('FILTER RESULTS', on_press=self.filter_results, style=Pack(background_color='maroon', color='white', padding=(5, 10)))
        clear_button = toga.Button('Clear Filters', on_press=self.clear_filters, style=Pack(padding=(5, 10)))

        # Create layout
        box = toga.Box(children=[
            toga.Label('FILTER BY:', style=Pack(padding=(10, 5), font_weight='bold', text_align=LEFT, color='red')),
            toga.Box(children=[
                toga.Label('Select Project:', style=Pack(padding=(5, 0), width=150, text_align=RIGHT)),
                self.project_select
            ], style=Pack(direction=ROW, padding=(5, 0))),
            toga.Box(children=[
                toga.Label('Select Contractor:', style=Pack(padding=(5, 0), width=150, text_align=RIGHT)),
                self.contractor_select
            ], style=Pack(direction=ROW, padding=(5, 0))),
            toga.Box(children=[
                toga.Label('Search by Keyword:', style=Pack(padding=(5, 0), width=150, text_align=RIGHT)),
                self.keyword_input
            ], style=Pack(direction=ROW, padding=(5, 0))),
            toga.Box(children=[
                toga.Label('Show Expired:', style=Pack(width=150, text_align=RIGHT)),
                self.show_expired
            ], style=Pack(direction=ROW, padding=(5, 0))),
            toga.Box(children=[
                toga.Label('Project Link Status:', style=Pack(padding=(5, 0), width=150, text_align=RIGHT)),
                self.project_status_select
            ], style=Pack(direction=ROW, padding=(5, 0))),
            toga.Box(children=[
                toga.Label('', style=Pack(width=150)),
                self.onsite_checkbox,
                self.offsite_checkbox
            ], style=Pack(direction=ROW, padding=(5, 0))),
            toga.Box(children=[
                filter_button,
                toga.Label('', style=Pack(width=20)),
                clear_button
            ], style=Pack(direction=ROW, padding=(10, 0))),
        ], style=Pack(direction=COLUMN, padding=10))

        # Add the box to the main window
        self.add(box)

    def filter_results(self, widget):
        self.go_to_managerform(widget)
        print("Filter results")

    def clear_filters(self, widget):
        self.project_select.value = None
        self.contractor_select.value = None
        self.keyword_input.value = ''
        self.show_expired.value = False
        self.project_status_select.value = None
        self.onsite_checkbox.value = False
        self.offsite_checkbox.value = False

    def go_to_managerform(self, widget):
        self.app.switch_form("managerform")
