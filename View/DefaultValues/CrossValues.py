from View.Formating.ParseColor import ParseColor


class CrossValues:
    __parse_color = ParseColor()

    __color = __parse_color.getColor(1, 0, 0)

    @property
    def color(self):
        return self.__color
