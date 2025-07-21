from board import Board
from game import Game

def main():
    initial_board = [
        ["WR", "WN", "WB", "WQ", "WK", "WB", "WN", "WR"],
        ["WP", "WP", "WP", "WP", "WP", "WP", "WP", "WP"],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        ["BP", "BP", "BP", "BP", "BP", "BP", "BP", "BP"],
        ["BR", "BN", "BB", "BQ", "BK", "BB", "BN", "BR"],
    ]

    board = Board()
    board.setup_from_string_array(initial_board)
    game = Game(board)

    while game.is_in_progress():
        print(game)
        start_row, start_col, end_row, end_col = map(int, input("Enter your move (start_row start_col end_row end_col): ").split())
        result = game.move(start_row, start_col, end_row, end_col)
        if result:
            print(result)

if __name__ == "__main__":
    main()