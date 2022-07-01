#!/usr/bin/env python3
from flask import Flask

import chess

app = Flask(__name__)

# define chess board
board = chess.Board()

@app.route("/")
def home():
  ret= open("index.html").read()
  # replace start postion with board.fen() in `index.html`
  # start postion  
  # fen: https://en.wikipedia.org/wiki/Forsyth–Edwards_Notation
  # board.fen(): 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1'
  return ret.replace('start', board.fen())

if __name__ == "__main__":
  app.run(debug=True)
   
