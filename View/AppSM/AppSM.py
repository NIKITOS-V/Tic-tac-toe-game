from enum import Enum

from kivy.uix.screenmanager import ScreenManager, SlideTransition


class ScreenType(str, Enum):
    menu_screen = "Menu screen"
    game_screen = "Game screen"
    settings_screen = "Settings screen"


class DirectionType(str, Enum):
    right = "right"
    left = "left"


class AppSM(ScreenManager):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.transition = SlideTransition(duration=.6)

    def load_menu_screen(self, *args):
        if self.current == ScreenType.game_screen:
            self.transition.direction = DirectionType.right

        else:
            self.transition.direction = DirectionType.left

        self.current = ScreenType.menu_screen

    def load_game_screen(self, *args):
        self.transition.direction = DirectionType.left

        self.current = ScreenType.game_screen

    def load_settings_screen(self, *args):
        self.transition.direction = DirectionType.right

        self.current = ScreenType.settings_screen
