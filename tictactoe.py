from IPython.display import clear_output
#create a function to display the board
def display_board(board):
    clear_output()
    print(board[7]+'|'+board[8]+'|'+board [9])
    print(board[4]+'|'+board[5]+'|'+board [6])
    print(board[1]+'|'+board[2]+'|'+board [3])  
#determine players' markers.
def player_marker():
    mark = ' '
    while not (mark == 'X' or mark == 'O'):
        mark = input('Player_1 get to select X or O:').upper()
    if mark == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']
#function to put player's mark on the board
def position_display(board, position, mark):
    board[position] = mark
def winning_condition(board, mark):
    return ((board[1] == board[2] == board[3] == mark) or 
            (board[4] == board[5] == board[6] == mark) or
            (board[7] == board[8] == board[9] == mark) or
            (board[1] == board[4] == board[7] == mark) or
            (board[2] == board[5] == board[8] == mark) or
            (board[3] == board[6] == board[9] == mark) or
            (board[1] == board[5] == board[9] == mark) or
            (board[3] == board[5] == board[7] == mark))
#boolean check if its TRUE or FALSE
#board[position] equal to empty string then theres available spot to play
def empty_space(board, position):
    return board[position] == ' '
#check to see if board is full, boolean check
def full_board_check(board):
    for position in range(1,10):
        #calling space_check function, if space_check is TRUE then the board is not full (FALSE) 
        if empty_space(board, position):
            return False
    return True
#checking if player choice is taken or not
def player_choice(board):
    position = 0
    while position not in list(range(1,10)) or not empty_space(board,position):
        try:
            position = int(input('Select a position (1-9): '))
        except ValueError:
            print('Please enter an integer value')
        if position not in list(range(1,10)) or not empty_space(board,position):
            print('Sorry that is not a valid play, pick again')
    return position
