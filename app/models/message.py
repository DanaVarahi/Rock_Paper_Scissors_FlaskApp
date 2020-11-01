
def get_message(winner, game):
    if winner is None:
      message_title = "It's a draw."
      message_body = f"{game.player1.name} and {game.player2.name} both chose {game.player1.choice}." 
      
      
    else:
        message_title = f"{winner.name} is the winner!"
        message_body = f"{winner.name} has won with {winner.choice}."

    return {'title':message_title, 'body': message_body}
