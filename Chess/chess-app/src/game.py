from enums import Color, GameStatus

class Game:
    """The main class to control the Chess game flow."""
    def __init__(self, board, helper):
        self.helper = helper
        self.board = board
        self.current_turn = Color.WHITE
        self.status = GameStatus.IN_PROGRESS

    def move(self, startRow: int, startCol: int, endRow: int, endCol: int) -> str:
        if self.status != GameStatus.IN_PROGRESS:
            return "invalid"

        piece_to_move = self.board.get_piece(startRow, startCol)
        if piece_to_move is None: return "invalid"
        if piece_to_move.color != self.current_turn: return "invalid"
        
        target_piece = self.board.get_piece(endRow, endCol)
        if target_piece and target_piece.color == self.current_turn:
            return "invalid"
        
        if not piece_to_move.is_valid_move(self.board, (startRow, startCol), (endRow, endCol)):
            return "invalid"
        
        captured_piece_str = str(target_piece) if target_piece else ""
        
        if target_piece and target_piece.symbol == 'K':
            self.status = GameStatus.WHITE_WINS if target_piece.color == Color.BLACK else GameStatus.BLACK_WINS

        self.board.set_piece(endRow, endCol, piece_to_move)
        self.board.set_piece(startRow, startCol, None)

        if self.status == GameStatus.IN_PROGRESS:
            self.current_turn = Color.BLACK if self.current_turn == Color.WHITE else Color.WHITE

        return captured_piece_str

    def get_game_status(self) -> int:
        return self.status.value

    def get_next_turn(self) -> int:
        if self.status != GameStatus.IN_PROGRESS:
            return -1
        return self.current_turn.value