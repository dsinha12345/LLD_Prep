from sliding_piece import SlidingPiece
from piece import Piece
from typing import Tuple
from board import Board
from enums import Color

class Rook(SlidingPiece):
    def __init__(self, color: Color):
        super().__init__(color)
        self._symbol = 'R'

    def is_valid_move(self, board: Board, start: Tuple[int, int], end: Tuple[int, int]) -> bool:
        is_straight = start[0] == end[0] or start[1] == end[1]
        if not is_straight:
            return False
        return self._is_path_clear(board, start, end)