from View.Builders.GameScreenBuilder import GameScreenBuilder
from View.Builders.MenuScreenBuilder import MenuScreenBuilder
from View.Builders.SettingsScreenBuilder import SettingsScreenBuilder
from View.MainScreenManager import MainScreenManager


class ScreenManagerBuilder:
    def __init__(self):
        self.app = None

    def setApp(self, value):
        self.app = value

        return self

    def build(self):
        screenManager = MainScreenManager()

        screenManager.add_widget(
            MenuScreenBuilder()
            .setName(screenManager.menuScreenName)
            .build()
        )

        screenManager.add_widget(
            SettingsScreenBuilder()
            .setName(screenManager.settingsScreenName)
            .build()
        )

        screenManager.add_widget(
            GameScreenBuilder()
            .setName(screenManager.gameScreenName)
            .setApp(self.app)
            .build()
        )

        return screenManager
