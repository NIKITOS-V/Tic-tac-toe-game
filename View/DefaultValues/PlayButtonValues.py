from View.Formating.ParseColor import ParseColor


class PlayButtonValues:
    __parse_color = ParseColor()

    __color = __parse_color.getColor(17, 203, 39)
    __on_press_color = __parse_color.getColor(21, 113, 219)

    @property
    def color(self):
        return self.__color

    @property
    def on_press_color(self):
        return self.__on_press_color
