from kivy.lang import Builder
from kivy.uix.screenmanager import Screen


Builder.load_file("View/Game/GameView.kv")


class GameScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.__app = None

    def setApp(self, app):
        self.__app = app

    def back(self):
        self.manager.loadMenuScreen()
