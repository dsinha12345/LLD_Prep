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