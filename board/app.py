#!/usr/bin/env python3
from gevent.pywsgi import WSGIServer
from flask import Flask

import sys

sys.path.append("../")
from engine import get_move

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

@app.route("/newgame", methods=['POST'])
def newgame():
  board.reset()
  return board.fen()

@app.route("/computermove", methods=['POST'])
def computermove():
  if not board.is_game_over():
    board.push(get_move(board))
  else:
    return 'gameover'
  return board.fen()

if __name__ == "__main__":
  # TODO: gunicorn server
  app.run(debug=True)
