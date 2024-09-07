from kivy.clock import Clock
from kivy.graphics import Ellipse


class Ball(Ellipse):
    def __init__(self, radius, pos, suicide_func, move_duration, **kwargs):
        super().__init__(**kwargs)

        self.pos = pos
        self.size = [radius, radius]

        self.__suicide_func = suicide_func
        self.__move_duration = move_duration

        self.__postponement_before_suicide = .2

    def start_timer(self):
        Clock.schedule_once(
            self.suicide,
            self.__move_duration + self.__postponement_before_suicide
        )

    def suicide(self, *dt):
        self.__suicide_func(self)
