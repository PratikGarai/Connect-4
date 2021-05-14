from board import Board
import pygame
import sys

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
    for c in range(COLS):
        for r in range(ROWS):
            pygame.draw.rect(
                screen, BLUE, (c*SQUARE_SIZE, (r+1)*SQUARE_SIZE, 
                                SQUARE_SIZE, SQUARE_SIZE)
            )
            pygame.draw.circle(
                screen, BLACK, (c*SQUARE_SIZE+CIRCLE_OFFSET,
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
                # if turn == 0 :
                #     # Player 1 input
                #     flag = False
                #     while not flag :
                #         print(f'Player 1 , enter your selection(0-{b.cols}) : ', end="")
                #         col = int(input()) 
                #         flag = b.isvalidLocation(col)
                #         if flag : 
                #             b.drop_piece(b.getNextOpenRow(col), col, 1)

                #     if b.winning_move(1):
                #         print("Player 1 wins")
                #         break

                # else :
                #     # Player 2 input
                #     flag = False
                #     while not flag :
                #         print(f'Player 2 , enter your selection(0-{b.cols}) : ', end="")
                #         col = int(input()) 
                #         flag = b.isvalidLocation(col)
                #         if flag : 
                #             b.drop_piece(b.getNextOpenRow(col), col, 2)
                    
                #     if b.winning_move(2):
                #         print("Player 2 wins")
                #         break

                # b.print_board()
                # turn = (turn+1)%2
                print("Clicked")