import turtle

class Scoreboard(turtle.Turtle):
    def __init__(self, left_name, right_name):
        super().__init__()
        self.left_score = 0
        self.right_score = 0
        self.left_name = left_name
        self.right_name = right_name
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 600//2 - 40)
        self.update()

    def update(self):
        self.clear()
        self.write(f"{self.left_name}: {self.left_score}    {self.right_name}: {self.right_score}",
                   align="center", font=("Courier", 24, "normal"))

    def left_point(self):
        self.left_score += 1
        self.update()

    def right_point(self):
        self.right_score += 1
        self.update()
