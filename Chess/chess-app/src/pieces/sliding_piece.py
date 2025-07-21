from piece import Piece
from abc import ABC, abstractmethod
from typing import Tuple
from board import Board


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
                return False  # Path is blocked
            current_r += step_r
            current_c += step_c
        return True  # Path is clear