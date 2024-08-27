from accessify import private

from View.Formating.Errors import ColorError


class ParseColor:
    __minColorValue = 0
    __maxColorValue = 255

    @private
    def isCorrectValues(self, red, green, blue):
        return (
                self.__minColorValue <= red <= self.__maxColorValue and
                self.__minColorValue <= green <= self.__maxColorValue and
                self.__minColorValue <= blue <= self.__maxColorValue
        )

    def getColor(self, red, green, blue):
        if self.isCorrectValues(red, blue, green):
            return red / self.__maxColorValue, green / self.__maxColorValue, blue / self.__maxColorValue

        else:
            raise ColorError()
