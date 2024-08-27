from View.Menu.MenuScreen import MenuScreen


class MenuScreenBuilder:
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
        menuScreen = MenuScreen(self.__app)

        menuScreen.name = self.__name

        return menuScreen
