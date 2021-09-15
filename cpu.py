import random
from player import Player

class CPU(Player):

    def __init__(self, name, sign,gamemode) -> None:
        super().__init__(name, sign)
        self.gamemode = gamemode
    
    def make_move(self, board: list) -> None:
        if self.gamemode == "EASY":
            places = [0,1,2,3,4,5,6,7,8]
            place = random.choice(places)
            while board[place] != " ":
                del places[place]
                place = random.choice(places)
            board[place] = self.sign