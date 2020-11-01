from flask import render_template, request
from app import app
from app.models.game import Game
from app.models.player import Player


@app.route('/')
def index():
  return render_template('index.html', title='Home')

@app.route('/<choice1>/<choice2>')
def players(choice1=None,choice2=None):
    player1 =Player('Player1',choice1)
    player2 =Player('Player2',choice2)
   
    game = Game(player1, player2)   
    winner = game.return_winner()
    if winner is None:
      message_title = "It's a draw."
      message_body = f"{game.player1.name} and {game.player2.name} both chose {game.player1.choice}." 
      
      return render_template('result.html', title='Result', heading=message_title,description=message_body)
      
    else:
        message_title = f"{winner.name} is the winner!"
        message_body = f"{winner.name} has won with {winner.choice}."
        return render_template('result.html', title='Result', heading=message_title, description=message_body)
