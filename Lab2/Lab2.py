# student name: Zhi Chuen Tan 
# student number: 65408361
import random
from unittest.mock import sentinel

class TicTacToe:
    def __init__(self): # Use as is
        """ initializes data fields (board and played) 
            and prints the banner messages 
            and prints the initial board on the screen
        """
        self.board = [' '] * 9 # A list of 9 strings, one for each cell, 
                               # will contain ' ' or 'X' or 'O'
        self.played = set()    # Set (of cell num) already played: to keep track of the played cells 
        print("Welcome to Tic-Tac-Toe!")
        print("You play X (first move) and computer plays O.")
        print("Computer plays randomly, not strategically.")
        self.printBoard()

    def printBoard(self) -> None:
        """ prints the board on the screen based on the values in the self.board data field """
        print(self.board[0] + " | " + self.board[1] + " | "  + self.board[2] + "    0 | 1 | 2")
        print("--+---+--    --+---+--")
        print(self.board[3] + " | " + self.board[4] + " | "  + self.board[5] + "    3 | 4 | 5")
        print("--+---+--    --+---+--")
        print(self.board[6] + " | " + self.board[7] + " | "  + self.board[8] + "    6 | 7 | 8")


    def playerNextMove(self) -> None:
        """ prompts the player for a valid cell number; 
            error checks that the input is a valid cell number; 
            and prints the info and the updated self.board;
        """
        try:
            self.playerChoice = int(input("Next move for X (state a valid cell number): "))
            if self.board[self.playerChoice] != ' ':
                print("Must enter a valid cell number")
                self.playerChoice = int(input("Next move for X (state a valid cell number): "))
        except ValueError:
            print("Must be an integer")
        except IndexError:
            print("Must enter a valid cell number")
        
        self.board [self.playerChoice] = 'X'
        print("You chose cell " + str(self.playerChoice))
        self.printBoard()


    def computerNextMove(self) -> None:
        """ computer randomly chooses a valid cell, 
            and prints the info and the updated self.board 
        """
        self.computerChoice = random.randint(0, 8)

        while self.board[self.computerChoice] != ' ':
            self.computerChoice = random.randint(0, 8)
        
        self.board [self.computerChoice] = 'O'
        print("Computer chose cell " + str(self.computerChoice))
        self.printBoard()

    def hasWon(self, who: str) -> bool:
        """ returns True if who (being passed 'X' or 'O') has won, False otherwise """
        self.who = who
        
        if (self.board[0] == self.board[1] == self.board[2] == who) or (self.board[3] == self.board[4] == self.board[5] == who) or (self.board[6] == self.board[7] == self.board[8] == who) or (self.board[0] == self.board[4] == self.board[8] == who) or (self.board[2] == self.board[4] == self.board[6] == who):
            return True
        
        else:
            return False

    def terminate(self, who: str) -> bool:
        """ returns True if who (being passed 'X' or 'O') has won or if it's a draw, False otherwise;
            it also prints the final messages:
                 "You won! Thanks for playing." or 
                 "You lost! Thanks for playing." or 
                 "A draw! Thanks for playing."  
        """
        self.who = who

        if self.hasWon(self.who) and self.who == 'X':
            print("You won! Thanks for playing.")
            return True
        
        elif self.hasWon(self.who) and self.who == 'O':
            print("You lost! Thanks for playing.")
            return True

        elif (' ' not in self.board) and not self.hasWon(self.who):
            print("A draw! Thanks for playing.")
            return True

        else:
            return False



if __name__ == "__main__":  # Use as is
    ttt = TicTacToe()  # initialize a game
    while True:
        ttt.playerNextMove()            # X starts first
        if(ttt.terminate('X')): break   # if X won or a draw, print message and terminate
        ttt.computerNextMove()          # computer plays O
        if(ttt.terminate('O')): break   # if O won or a draw, print message and terminate