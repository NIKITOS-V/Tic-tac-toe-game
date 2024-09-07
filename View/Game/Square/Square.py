from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.button import Button

Builder.load_file("BgView.kv/Game/Square/SquareView.kv")


class Square(Button):
    def __init__(self, app, **kwargs):
        super().__init__(**kwargs)

        self.app = app
