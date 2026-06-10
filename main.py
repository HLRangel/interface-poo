from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.graphics import Color, Rectangle
from kivymd.uix.screen import MDScreen
from kivy.properties import ColorProperty

class GameRect(Widget):
    color = ColorProperty((1, 0, 0, 1))

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        with self.canvas:
            self.color_instruction = Color(*self.color)
            self.rect = Rectangle(pos=self.pos, size=self.size)

        self.bind(pos=self._update_rect, size=self._update_rect)
        self.bind(color=self._update_color)

    def _update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size

    def _update_color(self, *args):
        self.color_instruction.rgba = self.color

    def _draw_symbol(self, clickpos, symbolkind):
        symbol_size = (20, 20)

        symbol_pos = (
            clickpos[0] - symbol_size[0] / 2,
            clickpos[1] - symbol_size[1] / 2
        )

        with self.canvas:
            Color(0, 0, 1, 1)
            Rectangle(pos=symbol_pos, size=symbol_size)

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            local = self.to_local(*touch.pos)
            print(f"clicked at window={touch.pos}, local={local}")

            self._draw_symbol(touch.pos, "X")

            return True
        
        return super().on_touch_down(touch)


class GameScreen(MDScreen):
    def on_kv_post(self, base_widget):
        with self.canvas.before:
            self.bg = Rectangle(
                pos=self.pos,
                size=self.size,
                source='assets/images/background.png'
            )
        
        self.bind(pos=self._update_bg, size=self._update_bg)

        # game rect
        rect = GameRect(
            size_hint=(None, None),
            size=(400, 400),
            pos_hint={"center_x": 0.5, "center_y": 0.5},
        )

        self.add_widget(rect)

    def _update_bg(self, *args):
        self.bg.pos = self.pos
        self.bg.size = self.size

class BoardGameApp(MDApp):
    def build(self):
        return Builder.load_file("app/views/title.kv")


if __name__ == '__main__':
    BoardGameApp().run()