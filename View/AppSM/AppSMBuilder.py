from View.Game.GameBuilder import GameBuilder
from View.Menu.MenuBuilder import MenuBuilder
from View.Settings.SettingsBuilder import SettingsBuilder
from View.AppSM.AppSM import AppSM, ScreenType


class AppSMBuilder:
    def __init__(self):
        self.__app = None

    def setApp(self, value):
        self.__app = value

        return self

    def build(self):
        screenManager = AppSM()

        screenManager.add_widget(
            MenuBuilder()
            .setName(ScreenType.menu_screen)
            .setApp(self.__app)
            .build()
        )

        screenManager.add_widget(
            SettingsBuilder()
            .setName(ScreenType.settings_screen)
            .setApp(self.__app)
            .build()
        )

        screenManager.add_widget(
            GameBuilder()
            .setName(ScreenType.game_screen)
            .setApp(self.__app)
            .build()
        )

        return screenManager
