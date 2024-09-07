from View.Shader.ShaderButton import ShaderButton


class SettingsButton(ShaderButton):
    def __init__(self, app, **kwargs):
        self.__image_path = "View/Menu/Buttons/SettingsButton/ButtonImage.png"

        self.__app = app

        super().__init__(self.__image_path, self.__app.normal_settings_button_color, **kwargs)

