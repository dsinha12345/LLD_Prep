class King(Piece):
    def __init__(self, color: Color):
        super().__init__(color)
        self._symbol = 'K'

    def is_valid_move(self, board: Board, start: Tuple[int, int], end: Tuple[int, int]) -> bool:
        dr, dc = abs(start[0] - end[0]), abs(start[1] - end[1])
        return dr <= 1 and dc <= 1 and not (dr == 0 and dc == 0)