from typing import final

from kivy.animation import Animation
from kivy.base import EventLoop
from kivy.clock import Clock
from kivy.graphics import RenderContext
from kivy.properties import ListProperty
from kivy.uix.button import Button
from kivy.uix.image import Image


class ShaderButton(Button):
    current_color = ListProperty()

    NORMAL: final(str) = "normal"
    DOWN: final(str) = "down"

    def __init__(self, image_path, start_color, **kwargs):
        super().__init__(**kwargs)
        self.current_color = start_color

        self.__image = None

        self.__init__shader()
        self.__load_image(image_path)
        self.__start_shader()

    def __init__shader(self):
        EventLoop.ensure_window()

        self.canvas = RenderContext(
            use_parent_projection=True,
            use_parent_modelview=True
        )

        self.canvas.shader.source = "View/Shader/Shader.glsl"

    def __load_image(self, image_path):
        self.__image = Image(
            source=image_path,
            size=self.size,
            pos=self.pos
        )

        self.add_widget(self.__image)

    def __start_shader(self):
        Clock.schedule_interval(self.provide_color, 0)

    def __change_size(self, value):
        anim = Animation(
            size_hint_y=self.size_hint_y * value,
            size_hint_x=self.size_hint_x * value,
            duration=.1
        )

        anim.start(self)

    def __return_size(self):
        anim = Animation(
            size_hint_y=1,
            size_hint_x=1,
            duration=.1
        )

        anim.start(self)

    def provide_color(self, *dt):
        self.canvas["current_color"] = tuple(self.current_color)

    def change_color(self):
        pass

    def return_color(self):
        pass

    def on_size(self, instance,  size):
        self.__image.size = size

    def on_pos(self, *args):
        self.__image.pos = self.pos

    def on_state(self, *args):
        if self.state == self.DOWN:
            self.__change_size(0.9)
            self.change_color()

        else:
            self.__return_size()
            self.return_color()
