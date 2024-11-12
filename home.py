
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField
from kivy.lang import Builder

username_helper = """
MDTextField:
    hint_text : "Enter username: "
    width: 400
    size_hint_x: None
    icon_right: "account"
"""

password_helper = """
MDTextField:
    hint_text : "Enter password: "
    size_hint_x : None
    password: True
    width: 400
"""

class Demo(MDApp):

    def build(self):
        screen = Screen()

        box_layout = MDBoxLayout(
            orientation = "vertical",
            pos_hint = {"center_x":0.5, "center_y":0.5},
            size_hint = (None, None),
            spacing = 20
        )

        box_layout.width = 400

        login_label = MDLabel(
            text = "Login",
            pos_hint = {"center_x":0.5, "center_y":0.5}, 
            size_hint = (None, None)
        )

        username = Builder.load_string(username_helper)
        password = Builder.load_string(password_helper)


        box_layout.add_widget(login_label)
        box_layout.add_widget(username)
        box_layout.add_widget(password)

        screen.add_widget(box_layout)

        return screen
    

if __name__ == "__main__":
    Demo().run()