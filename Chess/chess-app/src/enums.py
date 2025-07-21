import enum

class Color(enum.Enum):
    """Enumeration for player colors."""
    WHITE = 0
    BLACK = 1

class GameStatus(enum.Enum):
    """Enumeration for the game's status."""
    IN_PROGRESS = 0
    WHITE_WINS = 1
    BLACK_WINS = 2