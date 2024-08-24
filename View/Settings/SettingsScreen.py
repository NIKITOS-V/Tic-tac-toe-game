from kivy.lang import Builder
from kivy.uix.screenmanager import Screen


Builder.load_file("View/Settings/SettingsView.kv")


class SettingsScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def back(self):
        self.manager.loadMenuScreen()
