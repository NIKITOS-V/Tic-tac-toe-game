from kivy.lang import Builder
from kivy.uix.screenmanager import Screen


Builder.load_file("View/Menu/MenuView.kv")


class MenuScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def loadGameScreen(self):
        self.manager.loadGameScreen()

    def loadSettingsScreen(self):
        self.manager.loadSettingsScreen()
