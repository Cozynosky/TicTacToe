import random
from player import Player

class CPU(Player):

    def __init__(self, name, sign,hardmode = False) -> None:
        super().__init__(name, sign)
        self.hardmode = hardmode
    
    def make_move(self, board: list) -> None:
        if self.hardmode:
            if board[4] == " ":
                board[4] = self.sign
            else:
                player_sign = 'X' if self.sign == 'O' else 'O'

                # CPU has a chance to win
                if len(winning_pos := self.check_instant_win(board,self.sign) ) > 0:
                    board[random.choice(winning_pos)] = self.sign
                # Player has a chance to 100% win
                elif len(winning_pos := self.check_instant_win(board,player_sign) ) > 0:
                    board[random.choice(winning_pos)] = self.sign
                # pick other good pos
                elif len(other_pos := self.check_the_best_pos(board,player_sign)):
                    board[random.choice(other_pos)] = self.sign
                else:
                    self.pick_any_pos(board)
        else:
            self.pick_any_pos(board)

    def check_instant_win(self,board,sign) -> list:
        possible_places = []
        # check rows for 100% win 
        for i in range(0,7,3):
            if board[i:i+3].count(sign) == 2 and " " in board[i:i+3]:
                for j in range(3):
                    if board[i+j] == " ":
                        possible_places.append(i+j)
        #check columns for 100%
        for i in range(3):
            if [board[i],board[i+3],board[i+6]].count(sign) == 2 and " " in [board[i],board[i+3],board[i+6]]:
                for j in range(0,7,3):
                    if board[i+j] == " ":
                        possible_places.append(i+j)
        #check diagonals
        if [board[0],board[4],board[8]].count(sign) == 2 and " " in [board[0],board[4],board[8]]:
            for i in range(0,9,4):
                if board[i] == " ":
                    possible_places.append(i)
        
        elif [board[2],board[4],board[6]].count(sign) == 2 and " " in [board[2],board[4],board[6]]:
            for i in range(2,7,2):
                if board[i] == " ":
                    possible_places.append(i)

        return possible_places

    def check_the_best_pos(self, board, player_sign):
        possible_places = []
        # check rows for 100% win 
        for i in range(0,7,3):
            if board[i:i+3].count(self.sign) == 1 and " " in board[i:i+3] and not player_sign in board[i:i+3]:
                for j in range(3):
                    if board[i+j] == " ":
                        possible_places.append(i+j)
        #check columns for 100%
        for i in range(3):
            if [board[i],board[i+3],board[i+6]].count(self.sign) == 1 and " " in [board[i],board[i+3],board[i+6]] and not player_sign in [board[i],board[i+3],board[i+6]]:
                for j in range(0,7,3):
                    if board[i+j] == " ":
                        possible_places.append(i+j)
        #check diagonals
        if [board[0],board[4],board[8]].count(self.sign) == 1 and " " in [board[0],board[4],board[8]] and not player_sign in [board[0],board[4],board[8]]:
            for i in range(0,9,4):
                if board[i] == " ":
                    possible_places.append(i)
        
        elif [board[2],board[4],board[6]].count(self.sign) == 1 and " " in [board[2],board[4],board[6]] and not player_sign in [board[2],board[4],board[6]]:
            for i in range(2,7,2):
                if board[i] == " ":
                    possible_places.append(i)

        return possible_places


    def pick_any_pos(self, board:list):
        empty_places = [i for i in range(9) if board[i] == " "]
        board[random.choice(empty_places)] = self.sign