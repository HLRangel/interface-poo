# app/controllers/game_controller.py
from app.models.classes import TicTacToe

class GameController:
    def __init__(self):
        self.game = None
        self.on_board_update = None

    def start_game(self, interactive: bool = True):
        self.game = TicTacToe(interactive=interactive)
        self._notify_view()

    """
    Método que a interface gráfica (KivyMD) vai chamar 
    quando o usuário clicar em uma célula.
    """
    def make_move(self, x: int, y: int) -> bool:
        if self.game and (x, y) in self.game.board.empty_cells():
            player_atual = self.game.players[0]
            self.game.board.place_piece(x, y, player_atual.piece_idx)
            
            self._notify_view()
            return True
        return False

    def get_board_state(self):
        if self.game:
            return self.game.board
        return None

    def _notify_view(self):
        if self.on_board_update and self.game:
            self.on_board_update(self.get_board_state())