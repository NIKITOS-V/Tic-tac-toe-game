from random import Random

from kivy.animation import Animation
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.uix.relativelayout import RelativeLayout

from View.Bg.Ball import Ball

Builder.load_file("View/Bg/BgView.kv")


class AnimatedBg(RelativeLayout):
    def __init__(self, app, **kwargs):
        super().__init__(**kwargs)

        self.__ball_start_y = 0
        self.__ball_start_x = 0

        self.__min_ball_x_for_suicide = 0

        self.__min_ball_move_duration = 3
        self.__max_ball_move_duration = 8

        self.__min_ball_radius_ratio = .05
        self.__max_ball_radius_ratio = .1

        self.__spawn_interval = .1

        self.__change_shade_duration = 3

        self.__random = Random()
        self.app = app

    def start_animation(self):
        Clock.schedule_interval(self.spawn_ball, self.__spawn_interval)
        Clock.schedule_once(self.dynamically_change_color)
        Clock.schedule_interval(self.dynamically_change_color, self.__change_shade_duration * 6)

    def dynamically_change_color(self, *dt):
        color_animation = Animation(bg_ball_color=[.7, .7, 0, .8], duration=self.__change_shade_duration)
        color_animation += Animation(bg_ball_color=[0, .7, 0, .8], duration=self.__change_shade_duration)
        color_animation += Animation(bg_ball_color=[0, .7, .7, .8], duration=self.__change_shade_duration)
        color_animation += Animation(bg_ball_color=[0, 0, .7, .8], duration=self.__change_shade_duration)
        color_animation += Animation(bg_ball_color=[.7, 0, .7, .8], duration=self.__change_shade_duration)
        color_animation += Animation(bg_ball_color=[.7, 0, 0, .8], duration=self.__change_shade_duration)

        color_animation.start(self.app)

    def __get_ball_radius(self):
        return int(
            self.__random.randrange(
                round(self.width * self.__min_ball_radius_ratio),
                round(self.width * self.__max_ball_radius_ratio)
            )
        )

    def __get_ball_start_x(self,  radius):
        return round(
            self.__random.randrange(
                self.__ball_start_x,
                round(self.width - radius)
            )
        )

    def __get_ball_start_y(self, radius):
        return round(self.__ball_start_y - radius)

    def __get_ball_y_for_suicide(self):
        return round(self.height)

    def __get_ball_x_for_suicide(self, radius):
        return round(
            self.__random.randrange(
                self.__min_ball_x_for_suicide,
                round(self.width - radius)
            )
        )

    def __get_ball_move_duration(self):
        int_part = self.__random.randrange(
            self.__min_ball_move_duration,
            self.__max_ball_move_duration
        )

        tenth_part = self.__random.randrange(0, 9) * .1

        return int_part + tenth_part

    def spawn_ball(self, *dt):
        radius = self.__get_ball_radius()

        move_duration = self.__get_ball_move_duration()

        ball = Ball(
            radius,
            [
                self.__get_ball_start_x(radius),
                self.__get_ball_start_y(radius)
            ],
            self.dell_ball,
            move_duration
        )

        self.canvas.add(ball)

        ball_animation = Animation(
            pos=[
                self.__get_ball_x_for_suicide(radius),
                self.__get_ball_y_for_suicide()
            ],
            duration=move_duration
        )

        ball_animation.start(ball)

        ball.start_timer()

    def dell_ball(self, ball):
        self.canvas.remove(ball)

    def on_size(self, *args):
        print(self.width, self.height)
