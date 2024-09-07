from kivy.base import EventLoop
from kivy.clock import Clock
from kivy.graphics import RenderContext
from kivy.uix.button import Button
from kivy.uix.image import Image


class ShaderButton(Button):
    def __init__(self, image_path, **kwargs):
        super().__init__(**kwargs)

        self.image = None

        self.image_path = image_path

        self.__init__shader()
        self.__load_image()
        self.__start_shader()

    def __init__shader(self):
        EventLoop.ensure_window()

        self.canvas = RenderContext(
            use_parent_projection=True,
            use_parent_modelview=True
        )

        self.canvas.shader.source = "View/Shader/Shader.glsl"

    def __load_image(self):
        self.image = Image(
            source=self.image_path,
            size=self.size
        )

        self.add_widget(self.image)

    def __start_shader(self):
        Clock.schedule_interval(self.provide_color, 0)

    def provide_color(self, *dt):
        pass

    def on_size(self, instance,  size):
        self.size = size
        self.image.size = size
