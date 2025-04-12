import turtle
from src.game import Game

def main():
    # Initialize the screen
    screen = turtle.Screen()
    screen.title("Pong Game")
    screen.bgcolor("black")
    screen.setup(width=800, height=600)
    screen.tracer(0)

    # Create and run the game
    game = Game(screen)
    game.run()

if __name__ == "__main__":
    main()
