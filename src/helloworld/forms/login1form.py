import toga
from toga.style import Pack
from toga.style.pack import COLUMN, CENTER

class Login1form(toga.Box):
    def __init__(self, app):
        super().__init__(style=Pack(direction=COLUMN, padding=10))
        self.app = app

        # Load the image
        logo_path = 'C:\\Users\\ntinl\\Downloads\\acciona.jpeg'
        logo_image = toga.Image(logo_path)
        logo_view = toga.ImageView(logo_image, style=Pack(width=200, height=100, padding=(20, 0), alignment=CENTER))

        # Create input boxes for email and password
        self.email_input = toga.TextInput(placeholder='email')
        self.password_input = toga.PasswordInput(placeholder='password')

        # Create labels
        self.message_label = toga.Label('')
        header_label = toga.Label('Sign in with your email and password', style=Pack(padding=(0, 5), text_align=CENTER))
        forgot_password_label = toga.Label('Forgot your password?', style=Pack(padding=(0, 5), text_align=CENTER))

        # Create button
        login_button = toga.Button('Sign in', on_press=self.login, style=Pack(padding_top=10))

        # Create a box to hold the input fields and buttons
        box = toga.Box(children=[
            logo_view,
            header_label,
            toga.Label('Email:', style=Pack(padding=(0, 5))),
            self.email_input,
            toga.Label('Password:', style=Pack(padding=(0, 5))),
            self.password_input,
            forgot_password_label,
            login_button,
            self.message_label
        ], style=Pack(direction=COLUMN, padding=10, alignment=CENTER))

        # Add the box to the form
        self.add(box)

    def login(self, widget):
        email = self.email_input.value
        password = self.password_input.value

        # Validate input fields
        if not email or not password:
            self.message_label.text = 'Email and password cannot be empty.'
            return

        # Simple validation
        if email.endswith('a') and password == 'a':
            # self.show_success_popup()
            self.go_to_inputform(widget)
        else:
            self.message_label.text = 'Invalid email or password.'

    def go_to_inputform(self, widget):
        print("Attempting to switch to inputform")
        self.app.switch_form("inputform")

#self.go_to_inputform(widget)
#on press self.login