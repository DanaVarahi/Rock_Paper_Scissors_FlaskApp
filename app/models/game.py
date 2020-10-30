class Game():
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

    
    def choice_comparison(self):
        choice1 = self.player1.choice
        choice2 = self.player2.choice
        
        if choice1 == 'scissors' and choice2 == 'paper':
            self.player1.winner = True

        elif choice1 == 'paper' and choice2 == 'rock':
            self.player1.winner = True

        elif choice1 == 'rock' and choice2 == 'scissors':
            self.player1.winner = True

        if choice2 == 'scissors' and choice1 == 'paper':
            self.player2.winner = True

        elif choice2 == 'paper' and choice1 == 'rock':
            self.player2.winner = True

        elif choice2 == 'rock' and choice1 == 'scissors':
            self.player2.winner = True

        
    def return_winner(self):
        self.choice_comparison()

        if self.player1.winner == True:
            return self.player1

        elif self.player2.winner == True:
            return self.player2

        else:
            return None