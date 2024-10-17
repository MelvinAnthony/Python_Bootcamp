def display_board(board):
    
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
#test_board = ['#','X','O','X','O','X','O','X','O','X']
#display_board(test_board)

#step 2 - Ask the user where to start x to o or o to x
def player_input():
    marker = ''
    
    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1: Do you want to be X or O? ').upper()

    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')
#print(player_input())

#step 3 - ask the user position where ot will store

def place_marker(board, marker, position):
    board[position] = marker
#test_board = ['#','X','O','X','O','X','O','X','O','X']
#place_marker(test_board,'$',8)
#display_board(test_board)

# step - 4 winning check 
def win_check(board,mark):
    
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal
#win_check(test_board,'X')

#step - 5 randomly start first
import random

def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'

#step 6 - space check wherather a space on board is free avilabile or not
def space_check(board, position):
    
    return board[position] == ' '

#step 7 - check wheather board if fully allociate

def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True
#step 8 - check where want to post the value 1 to 9
def player_choice(board):
    position = 0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input('Choose your next position: (1-9) '))
        
    return position

#step 9 - ask the user to play again
def replay():
    
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')

#step 10 - connect with all function
print("Welcome to X and O game")

while True:
    #reset the board
    theBoard = [' ']*10

    #players marker using player_input() function line number 18
    player1_marker,player2_marker = player_input()

    #give the turn using choose_first() function line number 58
    turn = choose_first()
    print(turn+ "Is go to first")

    #ask to user redy to play
    play_game = input('Are you ready to play? Enter Yes or No.')
    
    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False
    
    #After play game get true it make to play the game
    while game_on:
        #if it was a player 1 turn 

        if turn == 'Player 1':
            # Player1's turn.
            
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player1_marker, position)

            if win_check(theBoard, player1_marker):
                display_board(theBoard)
                print('Congratulations! You have won the game!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 2'

        else:
            #if it was a player 2 turn 
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player2_marker, position)

            if win_check(theBoard, player2_marker):
                display_board(theBoard)
                print('Player 2 has won!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 1'
    if not replay():
        break