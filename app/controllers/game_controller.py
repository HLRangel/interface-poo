# app/controllers/game_controller.py
from app.models.classes import TicTacToe

class HeadlessTicTacToe(TicTacToe):
    def __init__(self):
        super().__init__(True, True)

        self.putx = 0
        self.puty = 0

    def set_next_move(self, x, y):
        self.putx = x
        self.puty = y

    def headless_player_handler(self):
        return ["MOVE", self.putx, self.puty]

class GameController:
    def __init__(self):
        self.game = None

    def start_game(self, interactive: bool = True):
        self.game = HeadlessTicTacToe()

    """
    Método que a interface gráfica (KivyMD) vai chamar 
    quando o usuário clicar em uma célula.
    """
    def make_move(self, x: int, y: int):
        if self.game:
            self.game.set_next_move(x, y)

    def next(self):
        if self.game:
            self.game.update()

    def is_drawn(self):
        if self.game:
            return self.game.is_draw()
    
    def winner(self):
        if self.game:
            if self.game.winner_name == "none":
                return False
            else:
                return self.game.winner_name
                
    def get_board_state(self):
        if self.game:
            return self.game.board
        return None