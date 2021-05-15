import numpy as np 

class Board :
    def __init__(self, rows = 6, cols = 7):
        self.rows = rows
        self.cols = cols
        self.board = np.zeros((self.rows,self.cols))


    def drop_piece(self, row, col, piece) :
        self.board[row][col] = piece


    def isvalidLocation(self, col) :
        return col<self.cols and self.board[self.rows-1][col]==0


    def getNextOpenRow(self, col) :
        for r in range(self.cols):
            if self.board[r][col]==0:
                return r


if __name__=="__main__":
    b = Board()
    print(b.board)

    game_over = False
    turn = 0
    while not game_over :
        
        if turn == 0 :
            # Player 1 input
            flag = False
            while not flag :
                print(f'Player 1 , enter your selection(0-{b.cols}) : ', end="")
                col = int(input()) 
                flag = b.isvalidLocation(col)
                if flag : 
                    b.drop_piece(b.getNextOpenRow(col), col, 1)

        else :
            # Player 2 input
            flag = False
            while not flag :
                print(f'Player 2 , enter your selection(0-{b.cols}) : ', end="")
                col = int(input()) 
                flag = b.isvalidLocation(col)
                if flag : 
                    b.drop_piece(b.getNextOpenRow(col), col, 2)

        print(b.board)
        turn = (turn+1)%2