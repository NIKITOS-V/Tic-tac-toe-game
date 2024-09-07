from View.Formating.ParseColor import ParseColor


class GlobalValues:
    __parse_color = ParseColor()

    __default_bg_color = __parse_color.get_color(225, 223, 186)
    __default_bg_ball_color = __parse_color.get_color(255, 0, 0, .7)

    def __init__(self):
        self.__bg_color = self.__default_bg_color
        self.__bg_ball_color = self.__default_bg_ball_color

    @property
    def default_bg_color(self):
        return self.__default_bg_color

    @property
    def default_bg_ball_color(self):
        return self.__default_bg_ball_color

    def get_bg_color(self):
        return self.__bg_color

    def set_bg_color(self, red, green, blue):
        self.__bg_color = self.__parse_color.get_color(red, green, blue)


class PlayButtonValues:
    __parse_color = ParseColor()

    __default_pressed_color = __parse_color.get_color(21, 113, 219)
    __default_normal_color = __parse_color.get_color(17, 203, 39)

    def __init__(self):
        self.__normal_color = self.default_normal_color
        self.__pressed_color = self.default_pressed_color

    @property
    def default_normal_color(self):
        return self.__default_normal_color

    @property
    def default_pressed_color(self):
        return self.__default_pressed_color

    def get_normal_color(self):
        return self.__normal_color

    def det_pressed_color(self):
        return self.__pressed_color

    def set_pressed_color(self, red, green, blue):
        self.__pressed_color = self.__parse_color.get_color(red, green, blue)

    def set_normal_color(self, red, green, blue):
        self.__pressed_color = self.__parse_color.get_color(red, green, blue)


class SettingsButtonValues:
    __parse_color = ParseColor()

    __default_pressed_color = __parse_color.get_color(10, 10, 10)
    __default_normal_color = __parse_color.get_color(80, 80, 80)

    def __init__(self):
        self.__normal_color = self.default_normal_color
        self.__pressed_color = self.default_pressed_color

    @property
    def default_normal_color(self):
        return self.__default_normal_color

    @property
    def default_pressed_color(self):
        return self.__default_pressed_color

    def get_normal_color(self):
        return self.__normal_color

    def det_pressed_color(self):
        return self.__pressed_color

    def set_pressed_color(self, red, green, blue):
        self.__pressed_color = self.__parse_color.get_color(red, green, blue)

    def set_normal_color(self, red, green, blue):
        self.__pressed_color = self.__parse_color.get_color(red, green, blue)


class SquareValues:
    __parse_color = ParseColor()

    __default_outline_color = __parse_color.get_color(255, 153, 0)

    @property
    def default_outline_color(self):
        return self.__default_outline_color


class CrossValues:
    __parse_color = ParseColor()

    __color = __parse_color.get_color(1, 0, 0)

    @property
    def color(self):
        return self.__color


class ZeroValues:
    __parse_color = ParseColor()

    __color = __parse_color.get_color(0, 0, 1)

    @property
    def color(self):
        return self.__color
