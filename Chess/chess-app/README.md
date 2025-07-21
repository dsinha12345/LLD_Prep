# Chess Application

This project is a chess application that implements the game of chess using object-oriented programming principles. The application is structured to adhere to the SOLID principles, ensuring maintainability and scalability.

## Project Structure

```
chess-app
├── src
│   ├── __init__.py
│   ├── main.py          # Entry point for the chess application
│   ├── board.py         # Contains the Board class for managing the chessboard
│   ├── enums.py         # Defines Color and GameStatus enums
│   ├── game.py          # Controls the game flow and manages turns
│   ├── pieces           # Directory containing all chess piece classes
│   │   ├── __init__.py
│   │   ├── piece.py     # Abstract base class for all chess pieces
│   │   ├── sliding_piece.py # Base class for sliding pieces (Rook, Bishop, Queen)
│   │   ├── rook.py      # Rook piece implementation
│   │   ├── bishop.py    # Bishop piece implementation
│   │   ├── queen.py     # Queen piece implementation
│   │   ├── king.py      # King piece implementation
│   │   ├── knight.py     # Knight piece implementation
│   │   └── pawn.py      # Pawn piece implementation
│   └── utils.py         # Utility functions for the application
├── tests
│   ├── __init__.py
│   └── test_game.py     # Unit tests for the Game class
└── README.md             # Project documentation
```

## Setup Instructions

1. **Clone the Repository**
   ```
   git clone <repository-url>
   cd chess-app
   ```

2. **Install Dependencies**
   Ensure you have Python 3.x installed. You may want to create a virtual environment and install any necessary dependencies.

3. **Run the Application**
   To start the chess game, run the following command:
   ```
   python src/main.py
   ```

## Usage

Follow the prompts in the terminal to play the game. You will be able to make moves by specifying the starting and ending coordinates of the pieces.

## Testing

To run the tests, navigate to the `tests` directory and execute:
```
python -m unittest test_game.py
```

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.