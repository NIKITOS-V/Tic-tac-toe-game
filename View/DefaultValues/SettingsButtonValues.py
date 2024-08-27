from View.Formating.ParseColor import ParseColor


class SettingsButtonValues:
    __parse_color = ParseColor()

    __color = __parse_color.getColor(80, 80, 80)
    __on_press_color = __parse_color.getColor(30, 30, 30)

    @property
    def color(self):
        return self.__color

    @property
    def on_press_color(self):
        return self.__on_press_color
