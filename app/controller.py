from app.models.message import get_message
from flask import render_template, request
from app import app
from app.models.game import Game
from app.models.player import Player


@app.route('/')
def index():
  return render_template('index.html')

@app.route('/<choice1>/<choice2>')
def players(choice1=None,choice2=None):
    player1 =Player('Player1',choice1)
    player2 =Player('Player2',choice2)
   
    game = Game(player1, player2)   
    winner = game.return_winner()
    message = get_message(winner, game)

    return render_template('result.html',heading=message['title'], description=message['body'])

@app.route('/play', methods = ['GET', 'POST'])

def single_player():
  if request.method == 'GET':
    return render_template('play.html')

  else:
    players_name = request.form['name']
    players_choice = request.form['choice']

    player1 = Player(players_name, players_choice)
    player2 = Player('','')

    game = Game(player1, player2)
    game.set_computer_player()   
    winner = game.return_winner()
    message = get_message(winner, game)

    return render_template('result.html',heading=message['title'], description=message['body'])

