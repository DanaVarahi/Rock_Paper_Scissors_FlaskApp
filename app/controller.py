from flask import render_template, request
from app import app
from app.models.game import Game
from app.models.player import Player


@app.route('/')
def index():
   return "Let's play Rock Paper Scissors! Type both players choices in the url forwarded by a slash (eg. /rock) and press enter."

@app.route('/<choice1>/<choice2>')
def players(choice1=None,choice2=None):
    # return 'First player chose' + choice1 + ',' + 'Scond player chose' + choice2
   
    player1 =Player('Player1',choice1)
    player2 =Player('Player2',choice2)
   
    game = Game(player1, player2)   
    winner = game.return_winner()
    if winner is None:
        return "It's a draw."
    else:
        return f"{winner.name} has won with {winner.choice}."
