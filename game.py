import readchar
import os
import random

from player import Player
from cpu import CPU

clear = lambda: os.system("cls" if os.name == "nt" else "clear")


class Game:
    def __init__(self) -> None:
        self.reset_game()

    def reset_game(self) -> None:
        self.board_data = [" " for i in range(9)]
        self.signs = ['X','O']
        random.shuffle(self.signs)

    def run(self) -> None:
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
                |               1. 1P Mode [EASY]             |
                |               2. 1P Mode [HARD]             |
                |               3. 2P Mode                    |
                |               4. Exit                       |
                |                                             |
                +---------------------------------------------+"""
        )

        choice = readchar.readkey()
        if choice == "1":
            clear()
            self.P1 = Player(input("Write player name: "), self.signs[0])
            self.P2 = CPU("CPU", self.signs[1])
            self.play()
        elif choice == "2":
            clear()
            self.P1 = Player(input("Write player name: "), self.signs[0])
            self.P2 = CPU("CPU", self.signs[1], True)
            self.play()
        elif choice == "3":
            clear()
            self.P1 = Player(input("Write player 1 name: "), self.signs[0])
            clear()
            self.P2 = Player(input("Write player 2 name: "), self.signs[1])
            self.play()
        elif choice == "4":
            return 0
        else:
            clear()
            self.run()

    def print_board(self, board) -> None:
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

    def make_turn(self) -> None:
        print(f"\nPick place to write an {self.current_player.sign} [1-9]:")
        place_picked = int(readchar.readkey()) - 1
        if self.board_data[place_picked] == " ":
            self.board_data[place_picked] = self.current_player.sign
        else:
            print("Wrong place! Try again.")
            self.make_turn()

    def play(self):
        self.current_player = self.P1 if self.P1.sign == 'X' else self.P2
        mapping_data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.print_board(mapping_data)
        input("       Keybind mapping\n\n >> Press 'ENTER' to start << ")
        while (winning_sign := self.check_board()) == False:
            if self.current_player.name == "CPU":
                self.current_player.make_move(self.board_data)
            else:
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
        self.reset_game()
        self.run()
