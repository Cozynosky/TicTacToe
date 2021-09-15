import readchar
import os
import random

from player import Player

clear = lambda: os.system("cls" if os.name == "nt" else "clear")


class Game:
    def __init__(self):
        self.reset_board()

    def reset_board(self):
        self.board_data = [" " for i in range(9)]

    def run(self):
        print(
            """
                +---------------------------------------------+  
                |  _____ _     _____         _____            |
                | |_   _(_) __|_   _|_ _  __|_   _|__   ___   |
                |   | | | |/ __|| |/ _` |/ __|| |/ _ \ / _ \\  |
                |   | | | | (__ | | (_| | (__ | | (_) |  __/  |  
                |   |_| |_|\___||_|\__,_|\___||_|\___/ \___   |                        
                |                                             |
                |                    PRESS                    |
                |                  1. 1P Mode                 |
                |                  2. 2P Mode                 |
                |                  3. Exit                    |
                |                                             |
                +---------------------------------------------+"""
        )

        choice = readchar.readkey()
        if choice == "1":
            self.play()
        elif choice == "2":
            self.P1 = Player("Player 1", "X")
            self.P2 = Player("Player 2", "O")
            self.current_player = self.P1
            self.play()
        elif choice == "3":
            return 0
        else:
            clear()
            self.run()

    def print_board(self, board):
        clear()
        print(
            f"""
        +-----------+
        | {board[6]} | {board[7]} | {board[8]} |
        |---|---|---|
        | {board[3]} | {board[4]} | {board[5]} |
        |---|---|---|
        | {board[0]} | {board[1]} | {board[2]} |
        +-----------+
       """
        )

    def check_board(self):
        # check rows
        for i in range(0, 7, 3):
            if (
                self.board_data[i] == self.board_data[i + 1] == self.board_data[i + 2]
                and self.board_data[i] != " "
            ):
                return self.board_data[i]

        # check columns
        for i in range(3):
            if (
                self.board_data[i] == self.board_data[i + 3] == self.board_data[i + 6]
                and self.board_data[i] != " "
            ):
                return self.board_data[i]

        # check diagonals
        if (
            self.board_data[0] == self.board_data[4] == self.board_data[8]
            or self.board_data[2] == self.board_data[4] == self.board_data[6]
        ) and self.board_data[4] != " ":
            return self.board_data[4]

        return not " " in self.board_data

    def make_turn(self):
        print(f"\nPick place to write an {self.current_player.sign} [1-9]:")
        place_picked = int(readchar.readkey()) - 1
        if self.board_data[place_picked] == " ":
            self.board_data[place_picked] = self.current_player.sign
        else:
            print("Wrong place! Try again.")
            self.make_turn()

    def play(self):
        mapping_data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.print_board(mapping_data)
        input("       Keybind mapping\n\n >> Press 'ENTER' to start << ")
        while (winning_sign := self.check_board()) == False:
            self.print_board(self.board_data)
            print(f"        {self.current_player.name} turn.")
            self.make_turn()
            self.current_player = self.P1 if self.current_player == self.P2 else self.P2

        self.print_board(self.board_data)

        if winning_sign == True:
            input("""         IT'S A TIE!\n  Press 'ENTER' to continue.""")

        else:
            winner = self.P1 if winning_sign == self.P1.sign else self.P2
            input(f"""        {winner.name} wins!!\n  Press 'ENTER' to continue.""")

        clear()
        self.reset_board()
        self.run()
