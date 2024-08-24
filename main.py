from kivy.app import App

from View.ARLayout import ARLayout
from View.Builders.ScreenManagerBuilder import ScreenManagerBuilder


class TicTacToe(App):

    def build(self):
        arLayout = ARLayout()

        arLayout.add_widget(
            ScreenManagerBuilder()
            .setApp(self)
            .build()
        )

        return arLayout


if __name__ == "__main__":
    TicTacToe().run()
