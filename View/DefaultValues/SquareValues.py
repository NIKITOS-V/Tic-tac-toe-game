from View.Formating.ParseColor import ParseColor


class SquareValues:
    __parse_color = ParseColor()

    __outline_color = __parse_color.getColor(255, 153, 0)

    @property
    def outline_color(self):
        return self.__outline_color
