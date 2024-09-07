from View.Formating.ParseColor import ParseColor


class BgValues:
    __parse_color = ParseColor()

    __default_bg_color = __parse_color.get_color(225, 223, 186)

    __default_ball_alfa = .8
    __default_ball_shade = 230
    __default_change_shade_duration = 3
    __default_ball_spawn_interval = .2

    def __init__(self):
        self.__bg_color = self.__default_bg_color
        self.__shade = self.__default_ball_shade
        self.__duration = self.__default_change_shade_duration
        self.__alfa = self.__default_ball_alfa
        self.__spawn_interval = self.__default_ball_spawn_interval

    @property
    def default_ball_shade(self):
        return self.__default_ball_shade

    def get_ball_shade(self):
        return self.__shade

    def set_ball_shade(self, value):
        self.__shade = value

    @property
    def default_change_shade_duration(self):
        return self.__default_change_shade_duration

    def get_change_shade_duration(self):
        return self.__duration

    def set_change_shade_duration(self, value):
        self.__duration = value

    @property
    def default_ball_alfa(self):
        return self.__default_ball_alfa

    def get_ball_alfa(self):
        return self.__alfa

    def set_ball_alfa(self, value):
        self.__alfa = value

    @property
    def default_ball_spawn_interval(self):
        return self.__default_ball_spawn_interval

    def get_ball_spawn_interval(self):
        return self.__spawn_interval

    def set_ball_spawn_interval(self, value):
        self.__spawn_interval = value

    @property
    def default_bg_color(self):
        return self.__default_bg_color

    def get_bg_color(self):
        return self.__bg_color

    def set_bg_color(self, red, green, blue):
        self.__bg_color = self.__parse_color.get_color(red, green, blue)


class GlobalValues:
   pass


class PlayButtonValues:
    __parse_color = ParseColor()

    __default_pressed_color = __parse_color.get_color(21, 113, 219)
    __default_normal_color = __parse_color.get_color(17, 203, 39)

    __default_duration_of_change = .1
    __default_pressed_size_hint = .9

    def __init__(self):
        self.__normal_color = self.__default_normal_color
        self.__pressed_color = self.__default_pressed_color
        self.__duration_of_change = self.__default_duration_of_change
        self.__pressed_size_hint = self.__default_pressed_size_hint

    @property
    def default_normal_color(self):
        return self.__default_normal_color

    def get_normal_color(self):
        return self.__normal_color

    def set_normal_color(self, red, green, blue):
        self.__pressed_color = self.__parse_color.get_color(red, green, blue)

    @property
    def default_pressed_color(self):
        return self.__default_pressed_color

    def get_pressed_color(self):
        return self.__pressed_color

    def set_pressed_color(self, red, green, blue):
        self.__pressed_color = self.__parse_color.get_color(red, green, blue)

    @property
    def default_duration_of_change(self):
        return self.__default_duration_of_change

    def get_duration_of_change(self):
        return self.__duration_of_change

    def set_duration_of_change(self, value):
        self.__duration_of_change = value

    @property
    def default_pressed_size_hint(self):
        return self.__default_pressed_size_hint

    def get_pressed_size_hint(self):
        return self.__pressed_size_hint

    def set_pressed_size_hint(self, value):
        self.__default_pressed_size_hint = value


class SettingsButtonValues:
    __parse_color = ParseColor()

    __default_pressed_color = __parse_color.get_color(10, 10, 10)
    __default_normal_color = __parse_color.get_color(80, 80, 80)

    __default_duration_of_change = .1
    __default_pressed_size_hint = .9

    def __init__(self):
        self.__normal_color = self.__default_normal_color
        self.__pressed_color = self.__default_pressed_color
        self.__duration_of_change = self.__default_duration_of_change
        self.__pressed_size_hint = self.__default_pressed_size_hint

    @property
    def default_normal_color(self):
        return self.__default_normal_color

    def get_normal_color(self):
        return self.__normal_color

    def set_normal_color(self, red, green, blue):
        self.__pressed_color = self.__parse_color.get_color(red, green, blue)

    @property
    def default_pressed_color(self):
        return self.__default_pressed_color

    def get_pressed_color(self):
        return self.__pressed_color

    def set_pressed_color(self, red, green, blue):
        self.__pressed_color = self.__parse_color.get_color(red, green, blue)

    @property
    def default_duration_of_change(self):
        return self.__default_duration_of_change

    def get_duration_of_change(self):
        return self.__duration_of_change

    def set_duration_of_change(self, value):
        self.__duration_of_change = value

    @property
    def default_pressed_size_hint(self):
        return self.__default_pressed_size_hint

    def get_pressed_size_hint(self):
        return self.__pressed_size_hint

    def set_pressed_size_hint(self, value):
        self.__default_pressed_size_hint = value


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
