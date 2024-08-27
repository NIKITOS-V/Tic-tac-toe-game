from View.Game.GameScreenBuilder import GameScreenBuilder
from View.Menu.MenuScreenBuilder import MenuScreenBuilder
from View.Settings.SettingsScreenBuilder import SettingsScreenBuilder
from View.ScreenManager.AppScreenManager import MainScreenManager


class ScreenManagerBuilder:
    def __init__(self):
        self.__app = None

    def setApp(self, value):
        self.__app = value

        return self

    def build(self):
        screenManager = MainScreenManager()

        screenManager.add_widget(
            MenuScreenBuilder()
            .setName(screenManager.menuScreenName)
            .setApp(self.__app)
            .build()
        )

        screenManager.add_widget(
            SettingsScreenBuilder()
            .setName(screenManager.settingsScreenName)
            .setApp(self.__app)
            .build()
        )

        screenManager.add_widget(
            GameScreenBuilder()
            .setName(screenManager.gameScreenName)
            .setApp(self.__app)
            .build()
        )

        return screenManager
