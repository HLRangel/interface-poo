import random
import time

_game_global_id = 0

class GameObject:
    def __init__(self, otype):
        global _game_global_id

        self.type = otype

        self.id = _game_global_id
        _game_global_id += 1

class MoveRules:
    def __init__(self, vertsteps, horisteps, canskip):
        if isinstance(vertsteps, int):
            self.vertsteps = vertsteps
        else:
            self.vertsteps = 0
        if isinstance(horisteps, int):
            self.horisteps = horisteps
        else:
            self.horisteps = 0
        if isinstance(canskip, bool):
            self.can_skip_piece = canskip
        else:
            self.can_skip_piece = False


class Piece(GameObject):
    def __init__(self, name):
        super().__init__("Piece")

        self.name = name
        self.symbol = name[0]
        self.moveable = False
        self.set_move_rules(MoveRules(
            vertsteps=0,
            horisteps=0,
            canskip=False
        ))

    def set_move_rules(self, rules):
        self.move_rules = rules


class Board(GameObject):
    def __init__(self, width, height):
        super().__init__("Board")

        self.width = width
        self.height = height
        self.states = [
            Piece("default")
        ]

    def resetBoard(self):
        self.board = [self.states[0]] * (self.width * self.height)

    def move_piece(self, fromx, fromy, tox, toy):
        to_idx = toy * self.width + tox
        fr_idx = fromy * self.width + fromx
        
        if to_idx < len(self.board) and fr_idx < len(self.board):
            self.board[to_idx] = self.board[fr_idx]
            self.board[fr_idx] = self.states[0]
        else:
            raise ValueError("Invalid move.")


class Player(GameObject):
    def turn_update(self, states):
        if states[0][0] == "IDLE":
            return ["IDLE"]
        else:
            raise ValueError("Unexpected magic state.")

    def __init__(self, name):
        super().__init__("Player")

        self.name = name

class Game:
    def create_board(self):
        self.board = Board(3, 3)

    def __init__(self, player_arr):
        self.players = player_arr
        
        self.create_board()

    def update(self):
        # type, expected len
        for player in self.players:
            player.turn_update(
                [
                    ["IDLE", 0]
                ]
            )

# Tic-Tac-Toe game

class TTTPiece(Piece):
    def __init__(self, name):
        super().__init__(name)
        self.moveable = False


class TTTBoard(Board):
    def __init__(self):
        super().__init__(3, 3)
        self.states.append(TTTPiece("X"))   # states[1]
        self.states.append(TTTPiece("O"))   # states[2]
        self.resetBoard()

    def place_piece(self, x, y, piece_idx):
        idx = y * self.width + x
        if idx >= len(self.board) or self.board[idx] is not self.states[0]:
            raise ValueError("Invalid placement.")
        self.board[idx] = self.states[piece_idx]

    def get_cell(self, x, y):
        return self.board[y * self.width + x]

    def empty_cells(self):
        return [
            (x, y)
            for y in range(self.height)
            for x in range(self.width)
            if self.board[y * self.width + x] is self.states[0]
        ]

    def display(self):
        time.sleep(0.4)

        for y in range(self.height):
            row = [
                self.get_cell(x, y).symbol
                if self.get_cell(x, y) is not self.states[0]
                else "."
                for x in range(self.width)
            ]
            print(" | ".join(row))
            if y < self.height - 1:
                print("--+---+--")
        print()

class TTTBot(Player):
    def __init__(self, name="Bot"):
        super().__init__(name)
        self.board_ref = None
        self.piece_idx = None

    def turn_update(self, states):
        if states[0][0] == "MOVE":
            x, y = random.choice(self.board_ref.empty_cells())
            print(f"{self.name} joga ({x}, {y})")
            return ["MOVE", x, y]
        return super().turn_update(states)


class TTTPlayer(Player):
    def __init__(self, name="Player"):
        super().__init__(name)
        self.board_ref = None
        self.piece_idx = None

    def turn_update(self, states):
        if states[0][0] == "MOVE":
            while True:
                try:
                    raw = input(f"Vez do(a) {self.name}. <x> <y> (0-2): ").strip()
                    x, y = map(int, raw.split())
                    if (x, y) in self.board_ref.empty_cells():
                        return ["MOVE", x, y]
                    print("Ocupada! Tente de novo.")
                except (ValueError, IndexError):
                    print("Movimento inválido, forma correta: <x> <y>")
        return super().turn_update(states)


class TicTacToe(Game):
    def create_board(self):
        self.board = TTTBoard()

    def __init__(self, interactive):
        if interactive:
            super().__init__([TTTPlayer("Player"), TTTBot("Bot")])
        else:
            super().__init__([TTTBot("Bot 1"), TTTBot("Bot 2")])

        for i, player in enumerate(self.players):
            player.piece_idx = i + 1      # X = 1, O = 2
            player.board_ref = self.board

    def check_winner(self):
        lines = [
            [(0, 0), (1, 0), (2, 0)],
            [(0, 1), (1, 1), (2, 1)],
            [(0, 2), (1, 2), (2, 2)],
            [(0, 0), (0, 1), (0, 2)],
            [(1, 0), (1, 1), (1, 2)],
            [(2, 0), (2, 1), (2, 2)],
            [(0, 0), (1, 1), (2, 2)],
            [(2, 0), (1, 1), (0, 2)],
        ]
        for line in lines:
            cells = [self.board.get_cell(x, y) for x, y in line]
            if cells[0] is not self.board.states[0] and all(c is cells[0] for c in cells):
                return cells[0]
        return None

    def is_draw(self):
        return len(self.board.empty_cells()) == 0

    def update(self):
        for player in self.players:
            result = player.turn_update([["MOVE", 2]])

            if result[0] == "MOVE":
                self.board.place_piece(result[1], result[2], player.piece_idx)

            self.board.display()

            winner = self.check_winner()
            if winner:
                print(f"{winner.name} ganhou!")
                return False
            if self.is_draw():
                print("Empate!")
                return False

        return True

    def run(self):
        print("=== Jogo da Velha ===\n")
        self.board.display()
        while self.update():
            pass