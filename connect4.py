import numpy as np 

def create_board() :
    board = np.zeros((6,7))
    return board


def drop_piece() :
    pass


def isvalidLocation() :
    pass


def getNextOpenRow() :
    pass

if __name__=="__main__":
    board = create_board()
    print(board)

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