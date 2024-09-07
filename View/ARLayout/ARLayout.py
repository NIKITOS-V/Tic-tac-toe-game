from kivy.properties import NumericProperty
from kivy.uix.relativelayout import RelativeLayout


class ARLayout(RelativeLayout):
    ratio = NumericProperty(16 / 9.)

    def __init__(self, app, **kwargs):
        super().__init__(**kwargs)

        self.app = app

    def do_layout(self, *args):
        for child in self.children:
            self.apply_ratio(child)
        super(ARLayout, self).do_layout()

    def apply_ratio(self, child):
        # ensure the child don't have specification we don't want
        child.size_hint = None, None
        child.pos_hint = {"center_x": .5, "center_y": .5}

        # calculate the new size, ensure one axis doesn't go out of the bounds
        w, h = self.size
        h2 = w * self.ratio
        if h2 > self.height:
            w = h / self.ratio
        else:
            h = h2
        child.size = w, h

        self.app.main_layout_size = w, h
