from View.Formating.ParseColor import ParseColor


class GlobalValues:
    __parse_color = ParseColor()

    __bg_color = __parse_color.getColor(225, 223, 186)

    @property
    def bg_color(self):
        return self.__bg_color
