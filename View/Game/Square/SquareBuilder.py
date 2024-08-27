from View.Game.Square.Square import Square


class SquareBuilder:
    def __init__(self):
        self.__app = None

    def setApp(self, value):
        self.__app = value

        return self

    def build(self):
        return Square(self.__app)
