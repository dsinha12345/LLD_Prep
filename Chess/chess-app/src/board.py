from pieces import Piece, King, Queen, Rook, Bishop, Knight, Pawn
from typing import List, Optional
from enum import Color

class Board:
    def __init__(self):
        self.grid: List[List["Piece"]] = [[None for _ in range(8)] for _ in range(8)]
    
    def get_piece(self, row: int, col:int) -> Optional["Piece"]:
        if 0 <= row < 8 and 0 <= col < 8:
            return self.grid[row][col]
        return None
    
    def set_piece(self, row: int, col: int, piece: Optional["Piece"]):
        if 0 <= row < 8 and 0 <= col < 8:
            self.grid[row][col] = piece
    
    def setup_from_string_array(self, initial_board: List[List[str]]):
        pieceMap = {
            'K': King, 
            'Q': Queen, 
            'R': Rook, 
            'B': Bishop, 
            'H': Knight, 
            'P': Pawn
        }
        for r in range(8):
            for c in range(8):
                piece_str = initial_board[r][c]
                if piece_str:
                    color_char, type_char = piece_str[0], piece_str[1]
                    color = Color.WHITE if color_char == 'W' else Color.BLACK
                    self.grid[r][c] = pieceMap[type_char](color)