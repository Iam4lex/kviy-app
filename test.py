from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.core.window import Window
from kivymd.app import MDApp
from kivymd.uix.list import OneLineListItem

Window.size = (360, 640)  # Set window size for testing

KV = '''
ScreenManager:
    MainScreen:

<MainScreen>:
    name: "main"
    MDBoxLayout:
        orientation: 'vertical'
        
        MDTextField:
            id: search_field
            hint_text: "Search"
            on_text: app.filter_list(self.text)
            size_hint_y: None
            height: "48dp"
            pos_hint: {"center_x": 0.5}
        
        ScrollView:
            MDList:
                id: item_list
'''

class MainScreen(Screen):
    pass

class SearchApp(MDApp):
    def build(self):
        self.screen = Builder.load_string(KV)
        return self.screen

    def on_start(self):
        self.populate_list()

    def populate_list(self):
        items = ["Apple", "Banana", "Orange", "Grapes", "Strawberry", "Pineapple", "Mango", "Blueberry", "Peach"]
        for item in items:
            self.root.get_screen('main').ids.item_list.add_widget(OneLineListItem(text=item))

    def filter_list(self, query):
        item_list = self.root.get_screen('main').ids.item_list
        item_list.clear_widgets()
        items = ["Apple", "Banana", "Orange", "Grapes", "Strawberry", "Pineapple", "Mango", "Blueberry", "Peach"]
        filtered_items = [item for item in items if query.lower() in item.lower()]

        for item in filtered_items:
            item_list.add_widget(OneLineListItem(text=item))

if __name__ == "__main__":
    SearchApp().run()
