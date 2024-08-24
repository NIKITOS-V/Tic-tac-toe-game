from View.Settings.SettingsScreen import SettingsScreen


class SettingsScreenBuilder:
    def __init__(self):
        self.__name = None

    def setName(self, value):
        self.__name = value

        return self

    def build(self):
        settingsScreen = SettingsScreen()

        settingsScreen.name = self.__name

        return settingsScreen
