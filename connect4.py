import numpy as np

row_count = 6 
column_count = 7 #number of columns

def create_board():
    board = np.zeros((row_count,column_count)) 
    return board

def drop_piece(board, row, col, piece):
    board[row][col] = piece 

def is_valid_location(board, col):
    return board[row_count-1][col] == 0 

def get_next_open_row(board, col): 
    for r in range(row_count): 
        if board[r][col] == 0: 
            return r 

def print_board(board):  
    print(np.flip(board, 0)) 

def winning_move(board, piece):

    #check horizontal locations for winning move
    for c in range(column_count-3): 
        for r in range(row_count):
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                return True

    #check vertical locations
    for c in range(column_count): 
        for r in range(row_count-3): 
            if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece: 
                return True

    #check for positively sloped diagonals
    for c in range(column_count-3): 
        for r in range(row_count-3): 
            if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece: 
                return True

    #chek for negatively sloped diagonals
    for c in range(column_count-3): 
        for r in range(3, row_count-3): #starts from 3
            if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece: 
                return True

board = create_board()
print_board(board)

game_over = False 
turn = 0 
while not game_over:
   
    #Player one input
    if turn == 0: 
        col = int(input("Player 1. Select your column(0-6): "))

        if is_valid_location(board, col):  
            row = get_next_open_row(board, col) 
            drop_piece(board, row, col, 1) 

            if winning_move(board, 1):
                print("PLAYER 1 WINS!")
                game_over = True
                break

    #Player two input
    else:    
        col = int(input("Player 2. Select your column(0-6): "))

        if is_valid_location(board, col):  
            row = get_next_open_row(board, col) 
            drop_piece(board, row, col, 2) 

            if winning_move(board, 2):
                print("PLAYER 2 WINS!")
                game_over = True
                break

    print_board(board)

    turn += 1 
    turn = turn % 2 