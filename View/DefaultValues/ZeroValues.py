from View.Formating.ParseColor import ParseColor


class ZeroValues:
    __parse_color = ParseColor()

    __color = __parse_color.getColor(0, 0, 1)

    @property
    def color(self):
        return self.__color
