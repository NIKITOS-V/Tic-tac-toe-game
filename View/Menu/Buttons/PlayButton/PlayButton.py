from View.Shader.ShaderButton import ShaderButton


class PlayButton(ShaderButton):
    def __init__(self, app, **kwargs):
        self.__image_path = "View/Menu/Buttons/PlayButton/ButtonImage.png"

        self.__app = app

        super().__init__(self.__image_path, **kwargs)

    def provide_color(self, *dt):
        if self.state == "normal":
            self.canvas["current_color"] = tuple(self.__app.play_button_color)

        else:
            self.canvas["current_color"] = tuple(self.__app.on_press_play_button_color)
