#Margot Murvihill
#Professor Einakian
#Section 1
#Tictactoe Main 

import tictactoeFuncs

tictactoeFuncs.showWelcome()  
opponent=tictactoeFuncs.pickOpponent()   
print('The board positions are as follows:')
emptyBoard=tictactoeFuncs.createBoard()
tictactoeFuncs.printBoard(emptyBoard)
userLetter=tictactoeFuncs.pickLetter()
if userLetter=='X':
   opponentLetter='O'
elif userLetter=='O':
   opponentLetter='X'
board=[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
tictactoeFuncs.printBoard(board)
win_status=False
cnt=1
while cnt<10 and win_status==False:
   if cnt%2==0:
      letter='O'
   else:
      letter='X'
   if opponent==1:
      if letter=='X' and opponentLetter=='X':
         tictactoeFuncs.computer(letter, board)
      elif letter=='X' and userLetter=='X':
         tictactoeFuncs.getInput(letter, board)
      elif letter=='O' and opponentLetter=='O':
         tictactoeFuncs.computer(letter, board)
      elif letter=='O' and userLetter=='O':
         tictactoeFuncs.getInput(letter, board)
   else: 
      tictactoeFuncs.getInput(letter, board)
   while tictactoeFuncs.checkRows(letter, board)==True or tictactoeFuncs.checkCols(letter, board)==True or tictactoeFuncs.checkDiags(letter, board)==True:
      win_status=True
      tictactoeFuncs.checkWin(letter, win_status)
      break
   tictactoeFuncs.printBoard(board)
   cnt+=1
if win_status==False:
   print('There is a tie.')
