import sys
import chess.pgn
from utils import list_of_pgns, games_in_pgn

# Τοποθέτηση σε μια λίστα όλων των κινήσεων ενός παιχνιδιού
def demo():
    pgns = list_of_pgns("games")
    print(pgns)
    sel = 1  # αριθμός αρχείου pgn που θα ανοίξει
    games = games_in_pgn(pgns[sel])
    sel = 1  # αριθμός παιχνιδιού μέσα στο pgn αρχείο
    game = games[sel]
    print("GAME: ", game)
    print("MOVES: ", game.moves)


# Αλληλεπίδραση με το χρήστη για επιλογή ένός αρχείου pgn, επιλογή ενός παιχνιδιού μέσα σε αυτό και παρακολούθηση των κινήσεων του παιχνιδιού μια προς μια.
def user_demo():
    pgns = list_of_pgns("games")
    for i, pgn in enumerate(pgns):
        print(f"{i+1}. {pgn}")
    sel = input("Select pgn file: ")
    sel = int(sel) - 1
    games = games_in_pgn(pgns[sel])
    for i, game in enumerate(games):
        print(f"{i+1}. {game}")
    sel = input("Select game: ")
    sel = int(sel) - 1
    game = games[sel]
    print("GAME: ", game)
    for m, w, b in game.moves:
        print(f"{m} move, white: {w}, black: {b}")
        input("Press Enter to continue...")


# Αλληλεπίδραση με το χρήστη για επιλογή ένός αρχείου pgn, επιλογή ενός παιχνιδιού μέσα σε αυτό και παρακολούθηση των κινήσεων του παιχνιδιού μια προς μια και απεικόνιση του ταμπλό με το python-chess
def user_demo_plus_python_chess():
    pgns = list_of_pgns("games")
    for i, pgn in enumerate(pgns):
        print(f"{i+1}. {pgn}")
    sel = input("Select pgn file: ")
    sel = int(sel) - 1
    python_chess_pgn_fn = open(pgns[sel])
    games = games_in_pgn(pgns[sel])
    for i, game in enumerate(games):
        print(f"{i+1}. {game}")
    sel = input("Select game: ")
    sel = int(sel) - 1
    game = games[sel]
    print("GAME: ", game)
    # προχωράμε μέχρι το επιλεγμένο παιχνίδι μέσα στο αρχείο pgn που ανοίξαμε
    for _ in range(sel + 1):
        python_chess_game = chess.pgn.read_game(python_chess_pgn_fn)
    board = python_chess_game.board()
    print(board)
    moves = python_chess_game.mainline_moves()
    my_iter = iter(moves)
    for m, w, b in game.moves:
        print(f"{m} move, white: {w}, black: {b}")
        move_w = next(my_iter)
        board.push(move_w)
        move_b = next(my_iter)
        board.push(move_b)
        print(board)
        input("Press Enter to continue...")
    python_chess_pgn_fn.close()


if __name__ == "__main__":
    print(sys.argv)
    if len(sys.argv) == 1:
        demo()
        sys.exit(0)
    if sys.argv[1] == "1":
        demo()
    elif sys.argv[1] == "2":
        user_demo()
    elif sys.argv[1] == "3":
        user_demo_plus_python_chess()
