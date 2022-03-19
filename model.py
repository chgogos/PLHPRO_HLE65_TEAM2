class PgnGame():
    def __init__(self, event, white, black, result, moves):
        self.event = event
        self.white = white
        self.black = black
        self.result = result
        self.moves = moves
        
    def __str__(self):
        return f"{self.event} White: {self.white} Black: {self.black} Result: {self.result}"
        