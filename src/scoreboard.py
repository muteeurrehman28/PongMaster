from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.score_player_1 = 0
        self.score_player_2 = 0
        self.update_score()

    def update_score(self):
        """Update the score display on the screen"""
        self.clear()
        self.write(f"Player 1: {self.score_player_1}  Player 2: {self.score_player_2}", align="center", font=("Courier", 24, "normal"))

    def player_1_score(self):
        """Increase Player 1's score and update the display"""
        self.score_player_1 += 1
        self.update_score()

    def player_2_score(self):
        """Increase Player 2's score and update the display"""
        self.score_player_2 += 1
        self.update_score()

    def show_player_names(self, player1_name, player2_name):
        """Show the player names on the screen"""
        self.goto(0, 230)
        self.clear()
        self.write(f"Player 1: {player1_name} | Player 2: {player2_name}", align="center", font=("Courier", 18, "normal"))

    def display_winner(self, player1_name, player2_name):
        """Display the winner of the game"""
        self.goto(0, 0)
        if self.score_player_1 == 10:
            self.write(f"{player1_name} Wins!", align="center", font=("Courier", 30, "normal"))
        elif self.score_player_2 == 10:
            self.write(f"{player2_name} Wins!", align="center", font=("Courier", 30, "normal"))
        self.goto(0, -30)
        self.write("Game Over! Press 'R' to Restart", align="center", font=("Courier", 18, "normal"))

    def show_welcome_message(self):
        """Show the welcome message on the start screen"""
        self.goto(0, 100)
        self.clear()
        self.write("Welcome to Pong Master!", align="center", font=("Courier", 24, "normal"))
        self.goto(0, -100)
        self.write("Press Enter to Start", align="center", font=("Courier", 18, "normal"))
