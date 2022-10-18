import random
import pandas as pd
import chess

def engine_test(num_tests):
  """
  A function that will iterate through a prespeified amount of games. At each move for both black and white a move is randomly selected from a list of legal moves
  After all the games have been simulated a dictionary is returned from the function with the number of moves and outcome of each game.
  
  num_tests: number of games to be simulated
  """
  num_moves = []
  checkmate = []
  stalemate = []
  draw = []
  outcome = []

  for i in range(0,num_tests):
    board = chess.Board()
    counter = 0 

    while board.is_checkmate() == False and board.is_stalemate() == False and board.is_insufficient_material() == False:
      # choose a random move from the list of legal moves
      move = random.choice(list(board.legal_moves))

      # carry out the randomly chosen move
      board.push(move)
      counter += 1
    
    num_moves.append(counter)
    checkmate.append(board.is_checkmate())
    stalemate.append(board.is_stalemate())
    draw.append(board.is_insufficient_material())
    outcome.append(board.outcome())
    print(f"Move number: {counter}")
    print(f"Is checkmate : {board.is_checkmate()}")
    print(f"Is stalemate : {board.is_stalemate()}")
    print(f"Is draw : {board.is_insufficient_material()}")
    print(f"Outcome: {board.outcome()}")
    print(board)

  data = {"Moves": num_moves, "Checkmate":checkmate, "Stalemate":stalemate, "Draw":draw,"Outcome":outcome}
  return pd.DataFrame(data)
