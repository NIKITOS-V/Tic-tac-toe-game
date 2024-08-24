from View.Menu.MenuScreen import MenuScreen


class MenuScreenBuilder:
    def __init__(self):
        self.__name = None

    def setName(self, value):
        self.__name = value

        return self

    def build(self):
        menuScreen = MenuScreen()

        menuScreen.name = self.__name

        return menuScreen
