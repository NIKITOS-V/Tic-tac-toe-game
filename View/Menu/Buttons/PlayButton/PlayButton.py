from kivy.animation import Animation

from View.Shader.ShaderButton import ShaderButton


class PlayButton(ShaderButton):
    def __init__(self, app, **kwargs):
        self.__image_path = "View/Menu/Buttons/PlayButton/ButtonImage.png"

        self.__app = app

        super().__init__(self.__image_path, self.__app.normal_play_button_color, **kwargs)

    def change_color(self):
        print(1)
        anim = Animation(
            current_color=self.__app.pressed_play_button_color,
            duration=self.__app.play_button_duration_of_change
        )

        anim.start(self)

    def return_color(self):
        anim = Animation(
            current_color=self.__app.normal_play_button_color,
            duration=self.__app.play_button_duration_of_change
        )

        anim.start(self)

