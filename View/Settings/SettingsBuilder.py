from View.Settings.SettingsScreen import SettingsScreen


class SettingsBuilder:
    def __init__(self):
        self.__name = None
        self.__app = None

    def setName(self, value):
        self.__name = value

        return self

    def setApp(self, value):
        self.__app = value

        return self

    def build(self):
        settingsScreen = SettingsScreen(self.__app)

        settingsScreen.name = self.__name

        return settingsScreen
