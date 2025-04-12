import turtle
import random
import json
import time
import winsound  # For sound effects (Windows)

# Set up the screen
screen = turtle.Screen()
screen.title("PongMaster - A Classic Pong Game")
screen.bgcolor("#2c3e50")  # Dark background color
screen.setup(width=800, height=600)
screen.tracer(0)  # Turn off automatic screen updates to improve performance

# Global variables for scores, high scores, and game states
player1_score = 0
player2_score = 0
high_scores = {}
game_running = False

# Load high scores from a file
try:
    with open("high_scores.json", "r") as file:
        high_scores = json.load(file)
except FileNotFoundError:
    high_scores = {"player1": 0, "player2": 0}

# Ball settings
ball_speed = 0.2  # Increased speed
ball_direction = random.choice([1, -1])  # Random ball direction

# Paddle settings
paddle_speed = 30  # Faster paddles for smoother movement
paddle_height = 100

# Ball object
ball = turtle.Turtle()
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = ball_speed * ball_direction
ball.dy = ball_speed * random.choice([1, -1])

# Left paddle (Player 1)
left_paddle = turtle.Turtle()
left_paddle.shape("square")
left_paddle.color("white")
left_paddle.shapesize(stretch_wid=6, stretch_len=1)
left_paddle.penup()
left_paddle.goto(-350, 0)

# Right paddle (Player 2 / AI)
right_paddle = turtle.Turtle()
right_paddle.shape("square")
right_paddle.color("white")
right_paddle.shapesize(stretch_wid=6, stretch_len=1)
right_paddle.penup()
right_paddle.goto(350, 0)

# Score display
score_display = turtle.Turtle()
score_display.speed(0)
score_display.color("white")
score_display.penup()
score_display.goto(0, 250)
score_display.write(f"Player 1: {player1_score} Player 2: {player2_score}", align="center", font=("Courier", 24, "normal"))

# Function to update the score
def update_score():
    score_display.clear()
    score_display.write(f"Player 1: {player1_score} Player 2: {player2_score}", align="center", font=("Courier", 24, "normal"))

# Function to play sound
def play_sound(sound_type):
    if sound_type == "hit":
        winsound.PlaySound("hit_sound.wav", winsound.SND_FILENAME)
    elif sound_type == "score":
        winsound.PlaySound("score_sound.wav", winsound.SND_FILENAME)

# Function to move paddles
def move_left_paddle_up():
    y = left_paddle.ycor()
    if y < 250 - paddle_height / 2:
        left_paddle.sety(y + paddle_speed)

def move_left_paddle_down():
    y = left_paddle.ycor()
    if y > -250 + paddle_height / 2:
        left_paddle.sety(y - paddle_speed)

def move_right_paddle_up():
    y = right_paddle.ycor()
    if y < 250 - paddle_height / 2:
        right_paddle.sety(y + paddle_speed)

def move_right_paddle_down():
    y = right_paddle.ycor()
    if y > -250 + paddle_height / 2:
        right_paddle.sety(y - paddle_speed)

# AI for the right paddle (Player 2)
def ai_move():
    if player2_score < 3:  # Easy AI (early game)
        if right_paddle.ycor() < ball.ycor():
            move_right_paddle_up()
        if right_paddle.ycor() > ball.ycor():
            move_right_paddle_down()
    else:  # Harder AI (later game)
        if right_paddle.ycor() < ball.ycor() - 5:  # More precise
            move_right_paddle_up()
        if right_paddle.ycor() > ball.ycor() + 5:  # More precise
            move_right_paddle_down()

# Pause the game
def pause_game():
    global game_running
    game_running = False

def resume_game():
    global game_running
    game_running = True

# Restart the game
def restart_game():
    global player1_score, player2_score, game_running
    player1_score = 0
    player2_score = 0
    game_running = True
    ball.goto(0, 0)
    ball.dx = ball_speed * ball_direction
    ball.dy = ball_speed * random.choice([1, -1])
    update_score()

# Function to check for ball collisions
def ball_collision():
    global player1_score, player2_score
    # Check if the ball hits the paddles
    if ball.xcor() > 340 and ball.xcor() < 350 and (right_paddle.ycor() + paddle_height / 2 > ball.ycor() > right_paddle.ycor() - paddle_height / 2):
        ball.dx *= -1
        play_sound("hit")  # Play hit sound

    if ball.xcor() < -340 and ball.xcor() > -350 and (left_paddle.ycor() + paddle_height / 2 > ball.ycor() > left_paddle.ycor() - paddle_height / 2):
        ball.dx *= -1
        play_sound("hit")  # Play hit sound

    # Ball out of bounds (score points)
    if ball.xcor() > 390:
        player1_score += 1
        play_sound("score")  # Play score sound
        update_score()
        ball.goto(0, 0)
        ball.dx = ball_speed * ball_direction
        ball.dy = ball_speed * random.choice([1, -1])

    if ball.xcor() < -390:
        player2_score += 1
        play_sound("score")  # Play score sound
        update_score()
        ball.goto(0, 0)
        ball.dx = ball_speed * ball_direction
        ball.dy = ball_speed * random.choice([1, -1])

# Main Game Loop
def game_loop():
    global game_running
    if game_running:
        # Update ball position manually
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)

        ball_collision()

        if player2_score > high_scores.get("player2", 0):
            high_scores["player2"] = player2_score
            with open("high_scores.json", "w") as file:
                json.dump(high_scores, file)

        if player1_score > high_scores.get("player1", 0):
            high_scores["player1"] = player1_score
            with open("high_scores.json", "w") as file:
                json.dump(high_scores, file)

        # Call the AI move for Player 2
        ai_move()

        screen.update()

    # Recursively call the game loop to keep running
    screen.ontimer(game_loop, 10)

# Main Menu Display and rest of the code remain the same...

# Game Initialization
screen.listen()
screen.onkey(move_left_paddle_up, "w")  # Left paddle move up
screen.onkey(move_left_paddle_down, "s")  # Left paddle move down
screen.onkey(move_right_paddle_up, "Up")  # Right paddle move up
screen.onkey(move_right_paddle_down, "Down")  # Right paddle move down

# Initial call to show main menu
show_main_menu()
screen.mainloop()
