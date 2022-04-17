# παράδειγμα ανάγνωσης αρχείου pgn ως αρχείου κειμένου
# εντοπισμός πληροφοριών π.χ. παίκτες, κινήσεις


class ChessGame:
    pass


the_game = ChessGame()

with open("19921104-r29-fischer-spassky.pgn", "r") as fp:
    in_moves_data = False
    moves = ""
    for line in fp:
        if line.strip() == "":
            continue
        if "white" in line.lower():
            the_game.white_player = line.split('"')[1]
        if "black" in line.lower():
            the_game.black_player = line.split('"')[1]
        if "[result" in line.lower():
            in_moves_data = True
            continue
        if in_moves_data:
            moves += line


print(f"White: {the_game.white_player}")
print(f"Black: {the_game.black_player}")
print(moves)
