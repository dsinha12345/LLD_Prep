from typing import Tuple
from src.board import Board
from src.enums import Color
from src.pieces.sliding_piece import SlidingPiece

class Queen(SlidingPiece):
    def __init__(self, color: Color):
        super().__init__(color)
        self._symbol = 'Q'

    def is_valid_move(self, board: Board, start: Tuple[int, int], end: Tuple[int, int]) -> bool:
        is_straight = start[0] == end[0] or start[1] == end[1]
        is_diagonal = abs(start[0] - end[0]) == abs(start[1] - end[1])
        if not (is_straight or is_diagonal):
            return False
        return self._is_path_clear(board, start, end)