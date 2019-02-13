#Objective of this program is to create an error handled tic tac toe game.
#The game works by the inputs given by the user.
#The program creates a log file tttg.log in the same directory as of this file.
#The logging level has been set to INFO.
#Defining function to create the board.

#Importing the necessary libraries.
import logging
import time
import random 

#Setting up the logging configurations.
logging.basicConfig(filename='tttg.log' , level=logging.INFO,
                   format='%(process)d : %(message)s')


#Creating a function to display a board.
def display_board(board):

    logging.info('This log was created at {}'.format(time.asctime()))
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('-----------')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('-----------')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    
    logging.info(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    logging.info('-----------')
    logging.info(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    logging.info('-----------')
    logging.info(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])

#Defining a function to create user input to assign marker.
def player_input():
    marker = ''
    while (marker != 'X' and marker != 'O'):
        marker = input("Player 1, please choose from X and O : ")
        player1 = marker
    if player1 == 'X':
        return ('X','O')
    else:
        return ('O','X')     

#Defining a function to place the user's marker.
def place_marker(board,marker,position):
    board[position] = marker


#Defining a function to see if anyone has won.
def win_check(board,mark):
    
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or 
    (board[4] == mark and board[5] == mark and board[6] == mark) or 
    (board[1] == mark and board[2] == mark and board[3] == mark) or 
    (board[7] == mark and board[4] == mark and board[1] == mark) or 
    (board[8] == mark and board[5] == mark and board[2] == mark) or 
    (board[9] == mark and board[6] == mark and board[3] == mark) or 
    (board[7] == mark and board[5] == mark and board[3] == mark) or 
    (board[9] == mark and board[5] == mark and board[1] == mark)) 

#Defining a function to see which user will start first.
def choose_first():
    flip = random.randint(0,1)
    if flip == 0:
        return 'Player1 starts'
    else:
        return 'Player2 starts'

#Defining a function to check for spaces.
def space_check(board, position):
    return board[position] == ' '

#Defining a function to run full board check.
def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True

#Defining a function to allow user to place his/her marker according to the number chosen.
def player_choice(board):
    
    condition = True
    while condition:
            try:
       
                position = 0
    
                while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):       
                    position = int(input('Choose your next position: (1-9) '))
                
                condition=False
            except:
                print("You entered something invalid , whoops!")
                logging.info("You entered something invalid , whoops!")
        
    return position 


#Defining a replay function for user if he/she wats to play again.
def replay():
    
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')


print('Welcome to Tic Tac Toe!')

while True:
    theBoard = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' will go first.')
    logging.info(turn + ' will go first.')
    
    play_game = input('Are you ready to play? Enter Yes or No.')
    #A flag , game_on is created to start the game if the input is yes.
    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':
            # Player1's turn.
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player1_marker, position)

            if win_check(theBoard, player1_marker):
                display_board(theBoard)
                print('Player1 has won the game!')
                logging.info('Player1 has won the game!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    logging.info('The game is a draw!')
                    break
                else:
                    turn = 'Player 2'

        else:
            # Player2's turn.
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player2_marker, position)

            if win_check(theBoard, player2_marker):
                display_board(theBoard)
                print('Player 2 has won!')
                logging.info('Player 2 has won!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    logging.info('The game is a draw!')
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        break            