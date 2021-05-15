import numpy as np 

class Board :
    def __init__(self, rows = 6, cols = 7):
        self.rows = rows
        self.cols = cols
        self.board = np.zeros((self.rows,self.cols))


    def drop_piece(self) :
        pass


    def isvalidLocation(self, col) :
        pass


    def getNextOpenRow(self) :
        pass


if __name__=="__main__":
    b = Board()
    print(b.board)

    game_over = False
    turn = 0
    while not game_over :
        
        if turn == 0 :
            # Player 1 input
            print("Player 1 , enter your selection(0-6) : ", end="")
            col = int(input()) 

        else :
            # Player 2 input
            print("Player 2 , enter your selection(0-6) : ", end="")
            col = int(input()) 

        turn = (turn+1)%2