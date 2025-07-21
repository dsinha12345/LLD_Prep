def validate_coordinates(row: int, col: int) -> bool:
    return 0 <= row < 8 and 0 <= col < 8

def format_move(start: Tuple[int, int], end: Tuple[int, int]) -> str:
    start_square = chr(start[1] + ord('A')) + str(8 - start[0])
    end_square = chr(end[1] + ord('A')) + str(8 - end[0])
    return f"{start_square} to {end_square}"

def is_valid_piece_symbol(symbol: str) -> bool:
    valid_symbols = {'K', 'Q', 'R', 'B', 'H', 'P'}
    return symbol in valid_symbols