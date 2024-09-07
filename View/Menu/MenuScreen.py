from kivy.animation import Animation
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

from View.Menu.Buttons.PlayButton.PlayButton import PlayButton
from View.Menu.Buttons.SettingsButton.SettingsButton import SettingsButton


Builder.load_file("View/Menu/MenuView.kv")


class MenuScreen(Screen):
    def __init__(self, app, **kwargs):
        super().__init__(**kwargs)

        self.__app = app

        self.__play_button = None
        self.__settings_button = None

        self.__init_play_button()
        self.__init_settings_button()

    def __init_play_button(self):
        self.__play_button = PlayButton(self.__app)

        self.__play_button.on_press = self.loadGameScreen

        self.ids.play_button_layout.add_widget(self.__play_button)

    def __init_settings_button(self):
        self.__settings_button = SettingsButton(self.__app)

        self.ids.settings_button_layout.add_widget(self.__settings_button)

    def loadGameScreen(self):
        Clock.schedule_once(self.manager.load_game_screen, self.__app.play_button_duration_of_change)


    def loadSettingsScreen(self):
        self.manager.load_settings_screen()
