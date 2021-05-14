from board import Board
import pygame
import sys
import numpy as np

SQUARE_SIZE = 100
RADIUS = int(SQUARE_SIZE*0.9)//2
CIRCLE_OFFSET = SQUARE_SIZE//2
ROWS = 6
COLS = 7

BLUE = (0,0,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLACK = (0,0,0)


def draw_board(screen, board):
    board = np.flip(board, 0)
    for c in range(COLS):
        for r in range(ROWS):
            pygame.draw.rect(
                screen, BLUE, (c*SQUARE_SIZE, (r+1)*SQUARE_SIZE, 
                                SQUARE_SIZE, SQUARE_SIZE)
            )

            color = BLACK
            if board[r][c]==1:
                color = RED
            if board[r][c]==2:
                color = GREEN
            pygame.draw.circle(
                screen, color, (c*SQUARE_SIZE+CIRCLE_OFFSET,
                (r+1)*SQUARE_SIZE+CIRCLE_OFFSET), RADIUS
            )
    pygame.display.update()


if __name__=="__main__":
    pygame.init()
    width = COLS * SQUARE_SIZE
    height = (ROWS+1) * SQUARE_SIZE

    size = (width, height)
    screen = pygame.display.set_mode(size)

    b = Board(ROWS, COLS)
    game_over = False
    turn = 0

    draw_board(screen, b.board)

    while not game_over :

        for event in pygame.event.get():
            if event.type == pygame.QUIT :
                sys.exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos
                col = pos[0]//SQUARE_SIZE
                print(col)
                if turn == 0 :
                    # Player 1 input
                    print("Player 1's turn")
                    flag = b.isvalidLocation(col)
                    if flag : 
                        b.drop_piece(b.getNextOpenRow(col), col, 1)
                        draw_board(screen, b.board)
                        b.print_board()
                    else : 
                        continue 

                    if b.winning_move(1):
                        print("Player 1 wins")
                        game_over = True
                        break

                else :
                    # Player 2 input
                    print("Player 2's turn")
                    flag = b.isvalidLocation(col)
                    if flag : 
                        b.drop_piece(b.getNextOpenRow(col), col, 2)
                        draw_board(screen, b.board)
                        b.print_board()
                    else : 
                        continue
                    
                    if b.winning_move(2):
                        print("Player 2 wins")
                        game_over = True
                        break

                turn = (turn+1)%2