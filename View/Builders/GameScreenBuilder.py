from View.Game.GameView import GameScreen


class GameScreenBuilder:
    def __init__(self):
        self.__name = None

    def setName(self, value):
        self.__name = value

        return self

    def build(self):
        gameScreen = GameScreen()

        gameScreen.name = self.__name

        return gameScreen
