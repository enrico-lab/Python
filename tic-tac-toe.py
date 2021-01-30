from IPython.display import clear_output
clear_output()

player1 = input("Please pick a marker 'X' or 'O'")

position = int(input('Please enter a number'))

def display_board(board):
  print(board[7]+'|'+board[8]+'|'+board[9])
  print('------')
  print(board[4]+'|'+board[5]+'|'+board[6])
  print('------')
  print(board[1]+'|'+board[2]+'|'+board[3])


test_board = [' ']
display_board('board')

#def player_input():
