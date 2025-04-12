from src.game import Game

def main():
    # Create a Game object and initialize it
    game = Game()
    game.show_start_screen()  # Show the start screen and handle game start

    # Start the event loop that keeps the game running
    game.screen.mainloop()  # This will run the main event loop of the game

if __name__ == "__main__":
    main()
