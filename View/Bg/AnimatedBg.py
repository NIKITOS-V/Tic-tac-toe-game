from random import Random

from kivy.animation import Animation
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.properties import ListProperty
from kivy.uix.relativelayout import RelativeLayout

from View.Bg.Ball import Ball
from View.Formating.ParseColor import ParseColor

Builder.load_file("View/Bg/BgView.kv")


class AnimatedBg(RelativeLayout):
    __parse_color = ParseColor()

    ball_color = ListProperty([1, 0, 0, 1])

    def __init__(self, app, **kwargs):
        super().__init__(**kwargs)

        self.__ball_start_y = 0
        self.__ball_start_x = 0

        self.__min_ball_move_duration = 3
        self.__max_ball_move_duration = 8

        self.__min_ball_radius_ratio = .05
        self.__max_ball_radius_ratio = .1

        self.__random = Random()
        self.__app = app

    def __init_ball_color(self):
        self.ball_color = (
            self.__parse_color.get_color(
                self.__app.ball_shade,
                0,
                0,
                self.__app.ball_alfa
            )
        )

    def __build_change_shade_animation(self, red, green, blue):
        return Animation(
            ball_color=self.__parse_color.get_color(
                red,
                green,
                blue,
                self.__app.ball_alfa
            ),
            duration=self.__app.ball_change_shade_duration
        )

    def start_animation(self):
        Clock.schedule_interval(self.spawn_ball, self.__app.ball_spawn_interval)
        Clock.schedule_once(self.dynamically_change_color)
        Clock.schedule_interval(self.dynamically_change_color, self.__app.ball_change_shade_duration * 6)

    def dynamically_change_color(self, *dt):
        color_animation = self.__build_change_shade_animation(
            self.__app.ball_shade,
            0,
            0,
        )

        color_animation += self.__build_change_shade_animation(
            self.__app.ball_shade,
            self.__app.ball_shade,
            0
        )

        color_animation += self.__build_change_shade_animation(
            0,
            self.__app.ball_shade,
            0
        )

        color_animation += self.__build_change_shade_animation(
            0,
            self.__app.ball_shade,
            self.__app.ball_shade
        )

        color_animation += self.__build_change_shade_animation(
            0,
            0,
            self.__app.ball_shade
        )

        color_animation += self.__build_change_shade_animation(
            self.__app.ball_shade,
            0,
            self.__app.ball_shade
        )

        color_animation.start(self)

    def __get_ball_radius(self):
        return self.__random.randrange(
            round(self.__app.main_layout_size[0] * self.__min_ball_radius_ratio),
            round(self.__app.main_layout_size[0] * self.__max_ball_radius_ratio)
        )

    def __get_ball_start_x(self,  radius):
        return self.__random.randrange(
            round(self.__ball_start_x),
            round(self.width - radius)
        )

    def __get_ball_start_y(self, radius):
        return round(self.__ball_start_y - radius)

    def __get_ball_y_for_suicide(self):
        return round(self.height)

    def __get_ball_x_for_suicide(self, radius, start_x):
        return self.__random.randrange(
            round(start_x - self.width * .5),
            round(start_x + self.width * .5)
        )

    def __get_ball_move_duration(self):
        int_part = self.__random.randrange(
            self.__min_ball_move_duration,
            self.__max_ball_move_duration
        )

        tenth_part = self.__random.randrange(0, 9) * .1

        return int_part + tenth_part

    def __build_ball(self, radius, pos, move_duration):
        return Ball(
            radius,
            pos,
            self.dell_ball,
            move_duration
        )

    def __build_move_animation(self, pos_for_suicide, move_duration):
        return Animation(
            pos=pos_for_suicide,
            duration=move_duration
        )

    def spawn_ball(self, *dt):
        radius = self.__get_ball_radius()

        move_duration = self.__get_ball_move_duration()

        start_x = self.__get_ball_start_x(radius)
        start_y = self.__get_ball_start_y(radius)

        x_for_suicide = self.__get_ball_x_for_suicide(radius, start_x)
        y_for_suicide = self.__get_ball_y_for_suicide()

        ball = self.__build_ball(radius, [start_x, start_y], move_duration)

        self.canvas.add(ball)

        ball_animation = self.__build_move_animation([x_for_suicide, y_for_suicide], move_duration)

        ball_animation.start(ball)

        ball.start_timer()

    def dell_ball(self, ball):
        self.canvas.remove(ball)
