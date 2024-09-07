from kivy.lang import Builder
from kivy.uix.screenmanager import Screen


Builder.load_file("View/Game/GameView.kv")


class GameScreen(Screen):

    def back(self):
        self.manager.loadMenuScreen()
