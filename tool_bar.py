from kivymd.app import MDApp
from kivy.core.window import Window
from kivymd.uix.screen import Screen
from kivymd.uix.toolbar import MDTopAppBar


class Demo(MDApp):

    def build(self):

        screen = Screen()
        self.theme_cls.primary_palette = "Blue"

        tool_bar = MDTopAppBar(text="Demo app")


        screen.add_widget(tool_bar)


        return screen

if __name__ == "__main__":
    Demo().run()
