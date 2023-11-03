11
"""
Author: Darrien Guan
Date: Oct 31, 2023
Discription: Text based tic-tac-toe. Intelligent version coming soon! (Personal github)
"""

import random

def winner(board):
    """This function accepts the Tic-Tac-Toe board as a parameter.
    If there is no winner, the function will return the empty string "".
    If the user has won, it will return "X", and if the computer has
    won it will return "O"."""
    
    # Check rows for the winner
    for i in range(3):
        temp_board_val = ""
        
        for x in range(3):
            temp_board_val += board[i][x]
            
        if temp_board_val == "XXX":
            return "X"
        
        elif temp_board_val == "OOO":
            return "O"
    
    # Check columns for the winner
    for i in range(3):
        temp_board_val = ""
        
        for x in range(3):
            temp_board_val += board[x][i]
            
        if temp_board_val == "XXX":
            return "X"
        
        elif temp_board_val == "OOO":
            return "O"
    
    # Check diagonal (top-left to bottom-right) for winner
    if board[0][0] == "X" and board[1][1] == "X" and board[2][2] == "X":
        return "X"
    
    elif board[0][0] == "O" and board[1][1] == "O" and board[2][2] == "O":
        return "O"
    
    # Check diagonal (bottom-left to top-right) for winner
    if board[0][2] == "X" and board[1][1] == "X" and board[2][0] == "X":
        return "X"
    
    elif board[0][2] == "O" and board[1][1] == "O" and board[2][0] == "O":
        return "O"
    
    # No winner: return ""
    return ""

def display_board(board):
    """This function accepts the Tic-Tac-Toe board as a parameter.
    It will print the Tic-Tac-Toe board grid (using ASCII characters)
    and show the positions of any X's and O's. It also displays
    the column and row numbers on top and beside the board to help
    the user figure out the coordinates of their next move.
    This function does not return anything."""
    
    print("   1   2   3")
    print("1: "+board[0][0]+" | "+board[0][1]+" | "+board[0][2])
    print(" ---+---+---")
    print("2: "+board[1][0]+" | "+board[1][1]+" | "+board[1][2])
    print(" ---+---+---")
    print("3: "+board[2][0]+" | "+board[2][1]+" | "+board[2][2])
    print()

def make_user_move(board):
    """This function accepts the Tic-Tac-Toe board as a parameter.
    It will ask the user for a row and column. If the row and
    column are each within the range of 0 and 2, and that square
    is not already occupied, then it will place an "X" in that square."""
    valid_move = False
    
    while not valid_move:
        
        while True:
            try:
                row = int(input("What row would you like to move to (1-3):"))-1
                col = int(input("What col would you like to move to (0-3):"))-1
                break
            
            except:
                print("Please enter an integer from 0 to 2.")
        
        if 0<=row<=2 and 0<=col<=2 and board[row][col]==" ":
            board[row][col] = 'X'
            valid_move = True
        else:
            print("Sorry, invalid square. Please try again!\n")

def make_computer_move(board):
    """This function accepts the Tic-Tac-Toe board as a parameter.
    It will randomly pick row and column values between 0 and 2.
    If that square is not already occupied, it will place an "O"
    in that square. Otherwise, another random row and column
    will be generated."""
    
    valid_move = False

    # Code needed here...
    while not valid_move:
        
        row = random.randint(0,2)
        col = random.randint(0,2)
        
        if 0<=row<=2 and 0<=col<=2 and board[row][col]==" ":
            board[row][col] = 'O'
            valid_move = True

def main():
    """Our Main Game Loop:"""
    free_cells = 9
    users_turn = True
    
    ttt_board = [[" ", " ", " "],[" ", " ", " "],[" ", " ", " "]]
    
    while True:
        
        display_board(ttt_board)
        if users_turn:
            make_user_move(ttt_board)
            free_cells -= 1
            users_turn = False

        else:
            make_computer_move(ttt_board)
            users_turn = True
            free_cells -= 1
            
        if winner(ttt_board) == 'X':
            display_board(ttt_board)
            print("Y O U W O N !")
            break
            
        elif winner(ttt_board) == 'O':
            display_board(ttt_board)
            print("I W O N !")
            break
            
        elif free_cells == 0:
            print("S T A L E M A T E !")
            print("\n*** GAME OVER ***\n")
            break

# Start the game!
main()