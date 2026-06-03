# app/controllers/game_controller.py
from app.models.classes import TicTacToe  # <- Ajustado para o arquivo e classe reais da sua Fase 1

class GameController:
    def __init__(self):
        self.game = None
        self.on_board_update = None  # Callback para notificar a View (Interface)

    def start_game(self, interactive: bool = True):
        # O construtor do seu TicTacToe exige o parâmetro 'interactive' (True para Player vs Bot, False para Bot vs Bot)
        self.game = TicTacToe(interactive=interactive)
        self._notify_view()

    def make_move(self, x: int, y: int) -> bool:
        """
        Método que a interface gráfica (KivyMD) vai chamar quando o usuário clicar em uma célula.
        Isso evita o uso do 'input()' do terminal que congelaria a tela.
        """
        if self.game and (x, y) in self.game.board.empty_cells():
            # Identifica qual é o jogador da vez e posiciona a peça
            # (Adaptando a lógica de inserção direta para não quebrar a Fase 1)
            player_atual = self.game.players[0] # Simplificação inicial para teste
            self.game.board.place_piece(x, y, player_atual.piece_idx)
            
            self._notify_view()
            return True
        return False

    def get_board_state(self):
        # Retorna a instância do tabuleiro para a interface conseguir ler as dimensões e símbolos
        if self.game:
            return self.game.board
        return None

    def _notify_view(self):
        # Se a interface gráfica estiver observando, ela redesenha o tabuleiro
        if self.on_board_update and self.game:
            self.on_board_update(self.get_board_state())