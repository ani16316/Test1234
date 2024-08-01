import toga
from toga.style import Pack
from toga.style.pack import COLUMN, CENTER
from PIL import Image
from datetime import datetime
import qrcode
import os

class Introform(toga.Box):
    def __init__(self, app):
        super().__init__(style=Pack(direction=COLUMN, padding=10))
        self.app = app

        # Load the acciona log
        logo_path = 'C:\\Users\\ntinl\\Downloads\\acciona.jpeg'
        logo_image = toga.Image(logo_path)
        logo = toga.ImageView(logo_image, style=Pack(width=200, height=100, padding=(20, 0)))

        # Create the QR code
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data('https://www.beatapp.org')
        qr.make(fit=True)
        qr_image = qr.make_image(fill='black', back_color='white')

        # Save the QR code as an image file
        qr_path = os.path.join(os.path.dirname(__file__), 'qr_code.png')
        qr_image.save(qr_path)

        # Load the QR code image
        qr_toga_image = toga.Image(qr_path)
        qr_image_view = toga.ImageView(qr_toga_image, style=Pack(width=200, height=200, padding=20))

        # Welcome message
        self.label = toga.Label(
            'Welcome to Linked Site',
            style=Pack(padding=(10, 0), font_size=24, font_weight="bold", text_align=CENTER)
        )

        # Date input
        self.date_input = toga.TextInput(placeholder="YYYY-MM-DD", style=Pack(padding=5))
        self.date_input.on_change = self.validate_date

        # Login button
        self.button = toga.Button(
            'Login to LinkedSite',
            on_press=self.go_to_login1form,
            style=Pack(padding=(10, 0), font_size=14, background_color='red', color='white', width=300, height=50)
        )

        # Instructions button
        instructions_button = toga.Button(
            'Login Instructions',
            on_press=self.instructions,
            style=Pack(padding=(10, 0), color='blue')
        )

        # Contact information
        contact_label = toga.Label(
            'Forgot your password or having trouble signing in?\n'
            'Contact the Service Desk on (03) 9624 4236, or raise an incident via ServiceNow Portal',
            style=Pack(padding=(10, 0), font_size=12, text_align=CENTER)
        )

        # Mobile app access link
        mobile_app_access = toga.Button(
            'Get access to LinkedSite Mobile App',
            on_press=self.access_mobile_app,
            style=Pack(padding=(10, 0), color='blue')
        )

        # Create a box to hold the elements
        box = toga.Box(
            children=[
                logo,
                self.label,
                self.date_input,
                self.button,
                instructions_button,
                contact_label,
                mobile_app_access,
                qr_image_view
            ],
            style=Pack(direction=COLUMN, padding=10, alignment=CENTER)
        )

        # Add the box to the form
        self.add(box)

    def validate_date(self, widget):
        try:
            # Attempt to parse the date
            date = datetime.strptime(widget.value, '%Y-%m-%d')
            widget.style.background_color = 'white'  # Valid date
        except ValueError:
            widget.style.background_color = 'red'  # Invalid date

    def go_to_login1form(self, widget):
        self.app.switch_form("login1form")

    def instructions(self, widget):
        print("Instructions button pressed")

    def access_mobile_app(self, widget):
        print("Mobile app access button pressed")

# Uncomment the main function and the if block to run the application
# def main():
#     return MainApp('Form Switcher', 'org.beeware.formswitcher')

# if __name__ == '__main__':
#     main().main_loop()
