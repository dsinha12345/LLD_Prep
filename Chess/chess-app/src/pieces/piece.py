from abc import ABC, abstractmethod
from typing import Optional, List, Tuple
from enums import Color
from board import Board

class Piece(ABC):
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
    def is_valid_move(self, board: 'Board', start: Tuple[int, int], end: Tuple[int, int]) -> bool:
        pass

    def __str__(self) -> str:
        color_char = 'W' if self.color == Color.WHITE else 'B'
        return color_char + self.symbol