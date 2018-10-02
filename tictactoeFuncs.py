# Project 3 - Tic-Tac-Toe Simulator
# 
# Name: Margot Murvihill
# Instructor: S. Einakian 
# Section: 1

import random

#The function showWelcome displays the welcome message at the beginning of the
#tic tac toe simulator.
#none -> str
def showWelcome():
   print('Welcome to the Tic-Tac-Toe Simulator.')
   print('Your goal is to line up 3 of your tics in either a line or diagonal')
   print('You will pick either X or O. X will go first.')   
 
#The function createBoard will store the data in a board.
#none -> list
def createBoard():
   board=['1', '2', '3', '4', '5', '6', '7', '8', '9']
   return board

#The function printBoard will print the game.
#list -> list 
def printBoard(board):
   print(board [0], '|', board [1], '|', board [2])
   print('----------')
   print(board [3], '|', board [4], '|', board [5])
   print('----------')
   print(board [6], '|', board [7], '|', board [8])    

#The function pickLetter asks the user to pick 'X' or 'O'
#none -> str
def pickLetter():
   letter=str(input('Choose X or O: '))
   while letter != 'X' and letter != 'O':
      print('ERROR: Letter must be X or O.')
      letter=str(input('Choose X or O: '))
   return letter

#The function getInput asks the user to pick a number 1-9 and will return the
#board with the player's move
#str list -> list
def getInput(letter, board):
   place=int(input('Where would you like to place your letter (pick in range of 1-9): '))
   if place<1 or place>9:
      print('Invalid move! Location is already taken. Please try again.')
      place=int(input('Where would you like to place your letter (pick in range of 1-9): '))
   else:
      pass
   while (board [place-1]=='X' or board [place-1]=='O'):
      print('Invalid move! Location is already taken. Please try again.')
      place=int(input('Where would you like to place your letter (pick in range of 1-9): '))
      if place<1 or place>9:
         print('That is not a valid move! You need to enter a value between 1-9. Please try again.')
         place=int(input('Where would you like to place your letter(pick in range of 1-9): '))
      else:
         pass
   board.pop(place-1)
   board.insert(place-1, letter)
   return board, letter

#The function checkRows will check if a player has completed a row by looking for 3 trues or 
#3 falses in a row. If no player has completed a row, the function will be passed.
#str list -> bool
def checkRows(letter, board): 
   if (letter in board [0] and letter in board [1] and letter in board [2]):
      return True
   elif (letter in board [3] and letter in board [4] and letter in board[5]):
      return True
   elif (letter in board [6] and letter in board [7] and letter in board [8]):
      return True
   else:
      pass
   
#The function checkCols will check if a player has completed a column by looking for 3 trues
#or 3 falses in the slots of a column. If no player has completed a column, the function will
#be passed. 
#str list -> bool
def checkCols(letter, board):
   if (letter in board [0] and letter in board [3] and letter in board [6]):
      return True 
   elif (letter in board [1] and letter in board [4] and letter in board [7]):
      return True 
   elif (letter in board [2] and letter in board [5] and letter in board [8]):
      return True 
   else: 
      pass
   
#The function checkDiags will check if a player has completed a diagonal by looking for 3 trues
#or 3 falses in the slots of a diagonal. If no player has completed a diagonal, the function 
#will pass.
#str list -> bool 
def checkDiags(letter, board):
   if (letter in board [0] and letter in board [4] and letter in board [8]):
      return True
   elif (letter in board [2] and letter in board [4] and letter in board [6]):
      return True
   else:
      pass

#The function boardFull takes the board and determines if it is full or not
#list -> bool
def boardFull(board):
   if board[0]!=' ' and board[1]!=' ' and board[2]!=' ' and board[3]!=' ' and board[4]!=' ' and board[5]!=' ' and board[6]!=' ' and board[7]!=' ' and board[8]!=' ':
      return True  
   
#The function checkWin will call the previous 3 check functions to see if any are true and 
#there is a winner.
#str list -> bool
def checkWin (letter, win_status):
   win_status = True
   if win_status == True:
      print(letter, 'Has won Tic-Tac-Toe!')
      return win_status
   else:
      pass
   
#The function turnCount takes the count and returns the counter.    
#none -> int
def turnCount(turn):
   if turn%2!=0:
      print("It's Player 1's (X's) turn!")
   else:
      print("It's Player 1's (O's) turn!")

#The function pickOpponent will ask the user if they want to play against the 
#computer or against a friend. 
#none -> int
def pickOpponent():
   opponent=int(input('Do you want to play with (1) computer or (2) player? (select 1 or 2): '))
   while opponent>2 or opponent<1:
      print('You must select (1) computer or (2) player. Please try again.')
      opponent=int(input('Do you want to play with (1) computer or (2) player? (select 1 or 2): '))
   return opponent

#The function computer will return a board with the randomized computer move, just like the
#function getInput
#str list -> list
def computer(letter, board):
   print ('Computer Turn: ')
   place=random.randint(0,9)
   while ('X' in board [place] or 'O' in board [place]):
      place=random.randint(0,9)
   board.pop(place)
   board.insert(place, letter)
   return board, letter
