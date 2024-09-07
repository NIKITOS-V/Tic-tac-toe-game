from kivy.animation import Animation
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

from View.Menu.Buttons.PlayButton.PlayButton import PlayButton
from View.Menu.Buttons.SettingsButton.SettingsButton import SettingsButton


Builder.load_file("View/Menu/MenuView.kv")


class MenuScreen(Screen):
    def __init__(self, app, **kwargs):
        super().__init__(**kwargs)

        self.app = app

        self.play_button = None
        self.settings_button = None

        self.__init_play_button()
        self.__init_settings_button()

    def __init_play_button(self):
        self.play_button = PlayButton(self.app)

        self.play_button.on_press = self.loadGameScreen

        self.ids.PlayButtonLayout.add_widget(self.play_button)

    def __init_settings_button(self):
        self.settings_button = SettingsButton(self.app)

        self.ids.SettingsButtonLayout.add_widget(self.settings_button)

    def loadGameScreen(self):
        self.manager.loadGameScreen()

    def loadSettingsScreen(self):
        self.manager.loadSettingsScreen()
