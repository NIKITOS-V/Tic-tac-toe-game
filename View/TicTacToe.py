from kivy.app import App
from kivy.properties import ListProperty

from View.ARLayout.ARLayout import ARLayout
from View.ScreenManager.ScreenManagerBuilder import ScreenManagerBuilder

from View.DefaultValues.GlobalValues import GlobalValues
from View.DefaultValues.PlayButtonValues import PlayButtonValues
from View.DefaultValues.SettingsButtonValues import SettingsButtonValues


class TicTacToeApp(App):
    bg_color = ListProperty()

    play_button_color = ListProperty()
    on_press_play_button_color = ListProperty()

    settings_button_color = ListProperty()
    on_press_settings_button_color = ListProperty()

    def __init__(self, presenter, **kwargs):
        super().__init__(**kwargs)
        self.presenter = presenter

        self.set_default_values()

    def set_default_values(self):
        self.bg_color = GlobalValues().bg_color

        self.play_button_color = PlayButtonValues().color
        self.on_press_play_button_color = PlayButtonValues().on_press_color

        self.settings_button_color = SettingsButtonValues().color
        self.on_press_settings_button_color = SettingsButtonValues().on_press_color

    def build(self):
        arLayout = ARLayout()

        arLayout.add_widget(
            ScreenManagerBuilder()
            .setApp(self)
            .build()
        )

        return arLayout
