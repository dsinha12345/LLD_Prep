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