from View.Shader.ShaderButton import ShaderButton


class SettingsButton(ShaderButton):
    def __init__(self, app, **kwargs):
        self.__image_path = "View/Menu/Buttons/SettingsButton/ButtonImage.png"

        self.app = app

        super().__init__(self.__image_path, **kwargs)

    def provide_color(self, *dt):
        if self.state == "normal":
            self.canvas["current_color"] = tuple(self.app.normal_settings_button_color)

        else:
            self.canvas["current_color"] = tuple(self.app.pressed_settings_button_color)
