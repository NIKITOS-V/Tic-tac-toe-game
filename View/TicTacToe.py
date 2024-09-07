from kivy.app import App
from kivy.properties import ListProperty

from View.ARLayout.ARLayout import ARLayout
from View.AppSM.AppSMBuilder import AppSMBuilder
from View.Bg.AnimatedBg import AnimatedBg

from View.Values.Values import *


class TicTacToeApp(App):
    bg_color = ListProperty()
    bg_ball_color = ListProperty()

    normal_play_button_color = ListProperty()
    pressed_play_button_color = ListProperty()

    normal_settings_button_color = ListProperty()
    pressed_settings_button_color = ListProperty()

    def __init__(self, presenter, **kwargs):
        super().__init__(**kwargs)

        self.presenter = presenter

        self.__global_values = None
        self.__play_button_values = None
        self.__settings_button_values = None

        self.__init_color_settings()
        self.set_default_values()

    def __init_color_settings(self):
        self.__global_values = GlobalValues()
        self.__play_button_values = PlayButtonValues()
        self.__settings_button_values = SettingsButtonValues()

    def set_default_values(self):
        self.bg_color = self.__global_values.default_bg_color
        self.bg_ball_color = self.__global_values.default_bg_ball_color

        self.normal_play_button_color = self.__play_button_values.default_normal_color
        self.pressed_play_button_color = self.__play_button_values.default_pressed_color

        self.normal_settings_button_color = self.__settings_button_values.default_normal_color
        self.pressed_settings_button_color = self.__settings_button_values.default_pressed_color

    def build(self):
        arLayout = ARLayout()

        animatedBd = AnimatedBg(
            self
        )

        appSM = (
            AppSMBuilder()
            .setApp(self)
            .build()
        )

        arLayout.add_widget(
            animatedBd
        )

        arLayout.add_widget(
            appSM
        )

        animatedBd.start_animation()

        return arLayout
