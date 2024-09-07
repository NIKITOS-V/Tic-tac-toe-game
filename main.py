from kivy.app import App
from kivy.properties import ListProperty, NumericProperty
from kivy.uix.relativelayout import RelativeLayout

from Model.Service import Service
from Presenter.Presenter import Presenter
from View.ARLayout.ARLayout import ARLayout
from View.AppSM.AppSMBuilder import AppSMBuilder
from View.Bg.AnimatedBg import AnimatedBg

from View.Values.Values import *


class TicTacToeApp(App):
    main_layout_size = ListProperty()

    bg_color = ListProperty()
    ball_alfa = NumericProperty()
    ball_shade = NumericProperty()
    ball_change_shade_duration = NumericProperty()
    ball_spawn_interval = NumericProperty()

    normal_play_button_color = ListProperty()
    pressed_play_button_color = ListProperty()
    play_button_pressed_size_hint = NumericProperty()
    play_button_duration_of_change = NumericProperty()

    normal_settings_button_color = ListProperty()
    pressed_settings_button_color = ListProperty()

    def __init__(self, presenter, **kwargs):
        super().__init__(**kwargs)

        self.presenter = presenter

        self.__bg_values = None
        self.__play_button_values = None
        self.__settings_button_values = None

        self.__init_color_settings()
        self.set_default_values()

    def __init_color_settings(self):
        self.__bg_values = BgValues()
        self.__play_button_values = PlayButtonValues()
        self.__settings_button_values = SettingsButtonValues()

    def set_default_values(self):
        self.bg_color = self.__bg_values.default_bg_color
        self.ball_shade = self.__bg_values.default_ball_shade
        self.ball_alfa = self.__bg_values.default_ball_alfa
        self.ball_change_shade_duration = self.__bg_values.default_change_shade_duration
        self.ball_spawn_interval = self.__bg_values.default_ball_spawn_interval

        self.normal_play_button_color = self.__play_button_values.default_normal_color
        self.pressed_play_button_color = self.__play_button_values.default_pressed_color
        self.play_button_pressed_size_hint = self.__play_button_values.default_pressed_size_hint
        self.play_button_duration_of_change = self.__play_button_values.default_duration_of_change

        self.normal_settings_button_color = self.__settings_button_values.default_normal_color
        self.pressed_settings_button_color = self.__settings_button_values.default_pressed_color

    def build(self):
        globalLayout = RelativeLayout()

        mainLayout = ARLayout(self)

        animatedBg = AnimatedBg(self)

        appSM = (
            AppSMBuilder()
            .setApp(self)
            .build()
        )

        globalLayout.add_widget(animatedBg)

        mainLayout.add_widget(appSM)

        globalLayout.add_widget(mainLayout)

        animatedBg.start_animation()

        return globalLayout


if __name__ == "__main__":
    service = Service()

    presenter = Presenter(service)

    view = TicTacToeApp(presenter)

    view.run()
