from utils import list_of_pgns, games_in_pgn

def demo():
    pgns = list_of_pgns("games")
    print(pgns)
    sel = 1 # αριθμός αρχείου pgn που θα ανοίξει
    games = games_in_pgn(pgns[sel])
    sel = 1 # αριθμός παιχνιδιού μέσα στο pgn αρχείο
    game = games[sel]
    print("GAME: ",  game)
    print("MOVES: ", game.moves)
    
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
    print("GAME: ",  game)
    for m,w,b in game.moves:
        print(f"{m} move, white: {w}, black: {b}")
        input("Press Enter to continue...")
    
if __name__=="__main__":
    demo()
    # user_demo()  
    
