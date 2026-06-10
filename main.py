from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.graphics import Color, Rectangle
from kivymd.uix.screen import MDScreen
from kivy.properties import ColorProperty

from app.controllers.game_controller import GameController

class GameRect(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        with self.canvas:
            self.rect = Rectangle(
                source='assets/images/neutral.png',
                pos=self.pos,
                size=self.size
            )

        self.bind(pos=self._update_rect, size=self._update_rect)

        self.visualstate = [
            "-", "-", "-",
            "-", "-", "-",
            "-", "-", "-"
        ]

        self.gamecontroller = GameController()
        self.gamecontroller.start_game(True)

        self.positions = []

    def _update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size

    def _draw_state(self):
        self.canvas.after.clear()
        self.positions = []

        symbol_size = (80, 80)
        cols = 3
        rows = 3
        gap = 60

        grid_w = cols * symbol_size[0] + (cols - 1) * gap
        grid_h = rows * symbol_size[1] + (rows - 1) * gap

        start_x = self.x + (self.width  - grid_w) / 2
        start_y = self.y + (self.height - grid_h) / 2

        state_images = {
            "-": "assets/images/neutral.png",
            "x": "assets/images/x.png",
            "o": "assets/images/o.png",
        }

        for i, state in enumerate(self.visualstate):
            col = i % cols
            row = i // cols

            state_pos_x = start_x + col * (symbol_size[0] + gap)
            state_pos_y = start_y + (rows - 1 - row) * (symbol_size[1] + gap)

            with self.canvas.after:
                Color(1, 1, 1, 1)
                Rectangle(
                    source=state_images[state],
                    pos=(state_pos_x, state_pos_y),
                    size=symbol_size
                )

            self.positions.append((state_pos_x, state_pos_y))

    def _click_change_state(self, pos):
        symbol_size = (80, 80)
        posn = 1

        for position in self.positions:
            if (position[0] <= pos[0] <= position[0] + symbol_size[0] and
                position[1] <= pos[1] <= position[1] + symbol_size[1]):
                
                if self.visualstate[posn - 1] == "-":
                    self.visualstate[posn - 1] = "x"
                    self.gamecontroller.make_move((posn - 1) % 3, (posn - 1) // 3)
            
                    self.gamecontroller.get_board_state().display()
            posn += 1

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            local = self.to_local(*touch.pos)
            print(f"clicked at window={touch.pos}, local={local}")

            self._click_change_state(touch.pos)
            self._draw_state()

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