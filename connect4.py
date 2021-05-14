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
    

    def print_board(self):
        b = np.flip(self.board, 0)
        print(b)


    def winning_move(self, piece):

        # Horizontal check
        for c in range(self.cols-3):
            for r in range(self.rows):
                if self.board[r][c]==piece and \
                    self.board[r][c+1]==piece and \
                    self.board[r][c+2]==piece and \
                    self.board[r][c+3]==piece :
                    return True
        
        # Vertical check
        for c in range(self.cols):
            for r in range(self.rows-3):
                if self.board[r][c]==piece and \
                    self.board[r+1][c]==piece and \
                    self.board[r+2][c]==piece and \
                    self.board[r+3][c]==piece :
                    return True
        
        # Top Left to Bottom Right check
        for c in range(self.cols-3):
            for r in range(self.rows-3):
                if self.board[r][c]==piece and \
                    self.board[r+1][c+1]==piece and \
                    self.board[r+2][c+2]==piece and \
                    self.board[r+3][c+3]==piece :
                    return True
        
        # Bottom Left to Top Right check
        for c in range(self.cols-3):
            for r in range(3, self.rows):
                if self.board[r][c]==piece and \
                    self.board[r-1][c+1]==piece and \
                    self.board[r-2][c+2]==piece and \
                    self.board[r-3][c+3]==piece :
                    return True


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

            if b.winning_move(1):
                print("Player 1 wins")
                break

        else :
            # Player 2 input
            flag = False
            while not flag :
                print(f'Player 2 , enter your selection(0-{b.cols}) : ', end="")
                col = int(input()) 
                flag = b.isvalidLocation(col)
                if flag : 
                    b.drop_piece(b.getNextOpenRow(col), col, 2)
            
            if b.winning_move(2):
                print("Player 2 wins")
                break

        b.print_board()
        turn = (turn+1)%2