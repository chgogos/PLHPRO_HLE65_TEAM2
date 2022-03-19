# αποθήκευση του ταμπλό σκακιού ως svg με το python-chess

import chess
import chess.pgn
import chess.svg


pgn = open("games/19921104-r29-fischer-spassky.pgn")

first_game = chess.pgn.read_game(pgn)

board = first_game.board()
for move in first_game.mainline_moves():
    board.push(move)

print(board) # εμφάνιση του ταμπλό στο τέλος του αγώνα
s = chess.svg.board(board, size=350)

svg_file = open("19921104-r29-fischer-spassky.svg", "w")
n = svg_file.write(s)
svg_file.close()
