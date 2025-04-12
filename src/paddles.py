import turtle

# Paddle class
class Paddle(turtle.Turtle):
    def __init__(self, x_position):
        super().__init__()
        self.speed(0)
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=6, stretch_len=1)
        self.penup()
        self.goto(x_position, 0)
        self.y_move = 0
        self.set_y_move(0)

    def set_y_move(self, move):
        """Sets the paddle's vertical speed (lower value for slower movement)"""
        self.y_move = move

    def move(self):
        """Moves the paddle continuously in the set direction"""
        y = self.ycor() + self.y_move
        
        # Ensure the paddle stops at the screen boundaries
        if y > 250:  # Adjusted to stop the paddle before going beyond the top edge
            self.sety(250)
        elif y < -250:  # Adjusted to stop the paddle before going beyond the bottom edge
            self.sety(-250)
        else:
            self.sety(y)

    def up(self):
        """Set upward movement"""
        self.set_y_move(1)  # Slow movement speed

    def down(self):
        """Set downward movement"""
        self.set_y_move(-1)  # Slow movement speed

    def stop(self):
        """Stop movement"""
        self.set_y_move(0)
