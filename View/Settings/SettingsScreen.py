from kivy.lang import Builder
from kivy.uix.screenmanager import Screen


Builder.load_file("View/Settings/SettingsView.kv")


class SettingsScreen(Screen):
    def __init__(self, app, **kwargs):
        super().__init__(**kwargs)

        self.app = app

    def back(self):
        self.manager.load_menu_screen()

    def ChangeText(self, app):
        app.text = "text"

