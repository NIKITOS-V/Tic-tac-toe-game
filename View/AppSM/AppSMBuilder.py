from View.Game.GameBuilder import GameBuilder
from View.Menu.MenuBuilder import MenuBuilder
from View.Settings.SettingsBuilder import SettingsBuilder
from View.AppSM.AppSM import AppSM


class ScreenManagerBuilder:
    def __init__(self):
        self.__app = None

    def setApp(self, value):
        self.__app = value

        return self

    def build(self):
        screenManager = AppSM()

        screenManager.add_widget(
            MenuBuilder()
            .setName(screenManager.menuScreenName)
            .setApp(self.__app)
            .build()
        )

        screenManager.add_widget(
            SettingsBuilder()
            .setName(screenManager.settingsScreenName)
            .setApp(self.__app)
            .build()
        )

        screenManager.add_widget(
            GameBuilder()
            .setName(screenManager.gameScreenName)
            .setApp(self.__app)
            .build()
        )

        return screenManager
