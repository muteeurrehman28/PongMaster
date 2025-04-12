import turtle
from src.paddles import Paddle
from src.ball import Ball

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.left_paddle = Paddle(-350, 0)
        self.right_paddle = Paddle(350, 0)
        self.ball = Ball()
        self.screen.listen()
        self.score_left = 0
        self.score_right = 0

    def run(self):
        while True:
            self.screen.update()
            self.ball.move()
            self.ball.check_bounce()
            self.check_collisions()
            self.update_score()
    
    def check_collisions(self):
        # Ball and paddle collision logic
        if self.ball.xcor() > 340 and self.ball.xcor() < 350 and self.ball.ycor() < self.right_paddle.ycor() + 50 and self.ball.ycor() > self.right_paddle.ycor() - 50:
            self.ball.setx(340)
            self.ball.dx *= -1
        
        if self.ball.xcor() < -340 and self.ball.xcor() > -350 and self.ball.ycor() < self.left_paddle.ycor() + 50 and self.ball.ycor() > self.left_paddle.ycor() - 50:
            self.ball.setx(-340)
            self.ball.dx *= -1

    def update_score(self):
        # Update score when the ball passes a paddle
        if self.ball.xcor() > 390:
            self.score_left += 1
            self.ball.goto(0, 0)
            self.ball.dx *= -1
        elif self.ball.xcor() < -390:
            self.score_right += 1
            self.ball.goto(0, 0)
            self.ball.dx *= -1
