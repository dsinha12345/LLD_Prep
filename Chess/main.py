import enum
from abc import ABC, abstractmethod
from typing import Optional, Tuple, List

# Helper classes and Enums
# =================================================================

class Color(enum.Enum):
    """Enumeration for player colors."""
    WHITE = 0
    BLACK = 1

class GameStatus(enum.Enum):
    """Enumeration for the game's status."""
    IN_PROGRESS = 0
    WHITE_WINS = 1
    BLACK_WINS = 2

class Board:
    """
    Represents the 8x8 chessboard.
    Manages the state and placement of pieces on the grid.
    """
    def __init__(self):
        self.grid: List[List[Optional['Piece']]] = [[None for _ in range(8)] for _ in range(8)]

    def get_piece(self, row: int, col: int) -> Optional['Piece']:
        if 0 <= row < 8 and 0 <= col < 8:
            return self.grid[row][col]
        return None

    def set_piece(self, row: int, col: int, piece: Optional['Piece']):
        if 0 <= row < 8 and 0 <= col < 8:
            self.grid[row][col] = piece
            
    def setup_from_string_array(self, initial_board: List[List[str]]):
        piece_map = {'K': King, 'Q': Queen, 'R': Rook, 'B': Bishop, 'H': Knight, 'P': Pawn}
        for r in range(8):
            for c in range(8):
                piece_str = initial_board[r][c]
                if piece_str:
                    color_char, type_char = piece_str[0], piece_str[1]
                    color = Color.WHITE if color_char == 'W' else Color.BLACK
                    self.grid[r][c] = piece_map[type_char](color)


# Abstract Base Classes for Pieces
# =====================================================================

class Piece(ABC):
    """An abstract base class for a chess piece."""
    def __init__(self, color: Color):
        self._color = color
        self._symbol = ''

    @property
    def color(self) -> Color:
        return self._color

    @property
    def symbol(self) -> str:
        return self._symbol

    @abstractmethod
    def is_valid_move(self, board: Board, start: Tuple[int, int], end: Tuple[int, int]) -> bool:
        pass

    def __str__(self) -> str:
        color_char = 'W' if self.color == Color.WHITE else 'B'
        return color_char + self.symbol

class SlidingPiece(Piece, ABC):
    """
    An abstract class for pieces that slide in straight lines (Rook, Bishop, Queen).
    It handles the logic for checking for obstructions along a path.
    """
    def _is_path_clear(self, board: Board, start: Tuple[int, int], end: Tuple[int, int]) -> bool:
        """Checks if the path between start and end is free of other pieces."""
        dr, dc = end[0] - start[0], end[1] - start[1]
        step_r = 0 if dr == 0 else dr // abs(dr)
        step_c = 0 if dc == 0 else dc // abs(dc)

        current_r, current_c = start[0] + step_r, start[1] + step_c
        while (current_r, current_c) != end:
            if board.get_piece(current_r, current_c) is not None:
                return False # Path is blocked
            current_r += step_r
            current_c += step_c
        return True # Path is clear


# Concrete Piece Implementations
# =========================================================================

class Rook(SlidingPiece):
    def __init__(self, color: Color):
        super().__init__(color)
        self._symbol = 'R'

    def is_valid_move(self, board: Board, start: Tuple[int, int], end: Tuple[int, int]) -> bool:
        # A rook moves in a straight line (horizontally or vertically).
        is_straight = start[0] == end[0] or start[1] == end[1]
        if not is_straight:
            return False
        return self._is_path_clear(board, start, end)

class Bishop(SlidingPiece):
    def __init__(self, color: Color):
        super().__init__(color)
        self._symbol = 'B'

    def is_valid_move(self, board: Board, start: Tuple[int, int], end: Tuple[int, int]) -> bool:
        # A bishop moves diagonally.
        is_diagonal = abs(start[0] - end[0]) == abs(start[1] - end[1])
        if not is_diagonal:
            return False
        return self._is_path_clear(board, start, end)

class Queen(SlidingPiece):
    def __init__(self, color: Color):
        super().__init__(color)
        self._symbol = 'Q'

    def is_valid_move(self, board: Board, start: Tuple[int, int], end: Tuple[int, int]) -> bool:
        # A queen moves in a straight line or diagonally.
        is_straight = start[0] == end[0] or start[1] == end[1]
        is_diagonal = abs(start[0] - end[0]) == abs(start[1] - end[1])
        if not (is_straight or is_diagonal):
            return False
        return self._is_path_clear(board, start, end)

# The following "Stepping" pieces do not inherit from SlidingPiece.
class King(Piece):
    def __init__(self, color: Color):
        super().__init__(color)
        self._symbol = 'K'

    def is_valid_move(self, board: Board, start: Tuple[int, int], end: Tuple[int, int]) -> bool:
        dr, dc = abs(start[0] - end[0]), abs(start[1] - end[1])
        return dr <= 1 and dc <= 1 and not (dr == 0 and dc == 0)

class Knight(Piece):
    def __init__(self, color: Color):
        super().__init__(color)
        self._symbol = 'H'

    def is_valid_move(self, board: Board, start: Tuple[int, int], end: Tuple[int, int]) -> bool:
        dr, dc = abs(start[0] - end[0]), abs(start[1] - end[1])
        return (dr == 1 and dc == 2) or (dr == 2 and dc == 1)

class Pawn(Piece):
    def __init__(self, color: Color):
        super().__init__(color)
        self._symbol = 'P'

    def is_valid_move(self, board: Board, start: Tuple[int, int], end: Tuple[int, int]) -> bool:
        start_r, start_c = start
        end_r, end_c = end
        target_piece = board.get_piece(end_r, end_c)
        direction = 1 if self.color == Color.WHITE else -1

        # Standard 1-step forward move
        if start_c == end_c and target_piece is None:
            if end_r == start_r + direction:
                return True
        # Diagonal capture
        if abs(start_c - end_c) == 1 and end_r == start_r + direction:
            if target_piece and target_piece.color != self.color:
                return True
        return False


# Main Solution Class (Game Controller)
# =====================================
class Solution:
    """The main class to control the Chess game flow."""
    def init(self, helper, chessboard: List[List[str]]):
        self.helper = helper
        self.board = Board()
        self.board.setup_from_string_array(chessboard)
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

    def getGameStatus(self) -> int:
        return self.status.value

    def getNextTurn(self) -> int:
        if self.status != GameStatus.IN_PROGRESS:
            return -1
        return self.current_turn.value