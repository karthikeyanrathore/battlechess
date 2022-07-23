#!/usr/bin/env python3
import random

def get_move(board):
  # TODO: make a real chess engine 
  # have a look at stockfish engine
  # https://github.com/official-stockfish/Stockfish
  move = random.choice(list(board.legal_moves))
  return move
