# Ανάγνωση αρχείου pgn με το python-chess library, 
# εμφάνιση στοιχείων αγώνα και ταμπλο

import chess.pgn

pgn = open("games/19921104-r29-fischer-spassky.pgn")

first_game = chess.pgn.read_game(pgn)

print(f'White: {first_game.headers["White"]}')
print(f'Black: {first_game.headers["Black"]}')

board = first_game.board()
print(board) # εμφάνιση του ταμπλό στην αρχή του αγώνα

for move in first_game.mainline_moves():
    board.push(move)
    print()

print(board) # εμφάνιση του ταμπλό στο τέλος του αγώνα
