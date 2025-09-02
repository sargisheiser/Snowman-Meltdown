from game_logic import play_game, prompt_yes_no

if __name__ == "__main__":
    while True:
        play_game()
        if not prompt_yes_no("Play again"):
            print("Thanks for playing Snowman Meltdown. Bye!")
            break