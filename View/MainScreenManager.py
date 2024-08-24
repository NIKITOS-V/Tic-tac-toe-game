from kivy.uix.screenmanager import ScreenManager, WipeTransition, SlideTransition


class MainScreenManager(ScreenManager):
    __right = "right"
    __left = "left"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.__menuScreenName = "Menu"
        self.__gameScreenName = "Game screen"
        self.__settingsScreenName = "Settings screen"

        self.transition = SlideTransition()

    @property
    def menuScreenName(self):
        return self.__menuScreenName

    @property
    def gameScreenName(self):
        return self.__gameScreenName

    @property
    def settingsScreenName(self):
        return self.__settingsScreenName

    def loadMenuScreen(self):
        if self.current == self.gameScreenName:
            self.transition.direction = self.__right

        else:
            self.transition.direction = self.__left

        self.current = self.__menuScreenName

    def loadGameScreen(self):
        self.transition.direction = self.__left

        self.current = self.__gameScreenName

    def loadSettingsScreen(self):
        self.transition.direction = self.__right

        self.current = self.__settingsScreenName
