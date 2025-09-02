import random
from ascii import STAGES

WORDS = ["python", "git", "github", "snowman", "meltdown"]

SEPARATOR = "-" * 40

def get_random_word():
    """Selects a random word from the list."""
    return random.choice(WORDS)

def mask_word(secret_word, guessed_letters):
    """Return masked representation with spaces for readability."""
    return " ".join(ch if ch in guessed_letters else "_" for ch in secret_word)

def display_game_state(mistakes, secret_word, guessed_letters):
    """Renders the current ASCII stage + masked word + metadata."""
    stage_index = min(mistakes, len(STAGES) - 1)
    remaining = (len(STAGES) - 1) - mistakes

    print(SEPARATOR)
    print(STAGES[stage_index])
    print(f"Word     : {mask_word(secret_word, guessed_letters)}")
    print(f"Guessed  : {' '.join(sorted(guessed_letters)) if guessed_letters else '-'}")
    print(f"Mistakes : {mistakes}/{len(STAGES) - 1}  |  Attempts left: {remaining}")
    print(SEPARATOR)

def normalize_guess(guess:str) -> str:
    """Normalize and validate a single-letter guess; return '' if invalid."""
    if guess is None:
        return ""
    guess = guess.lower().strip()
    if len(guess) != 1 or not guess.isalpha():
        return ""

    return guess

def is_word_resolved(secret_word, guessed_letters) -> bool:
    """Check if all letters of secret_word have been guessed."""
    return all(ch in guessed_letters for ch in secret_word)

def prompt_yes_no(message: str) -> bool:
    while True:
        resp = input(f"{message} (y/n): ").strip().lower()
        if resp in ("y", "yes"):
            return True
        if resp in ("n", "no"):
            return False
        print("Please answer with 'y' or 'n'.")

def play_game():

    secret_word = get_random_word()
    print("Welcome to Snowman Meltdown!")

    mistakes = 0
    max_mistakes = len(STAGES) - 1
    guessed_letters = set()

    while True:
        display_game_state(mistakes, secret_word, guessed_letters)
        guess = input("Guess a letter: ")
        guess = normalize_guess(guess)

        if not guess:
            print("Please enter exactly one letter (a-z).")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in secret_word:
            print("Nice correct letter!")
        else:
            mistakes += 1
            print("Nope that letter is not in the word.")

        if is_word_resolved(secret_word, guessed_letters):
            display_game_state(mistakes, secret_word, guessed_letters)
            print("Success: You saved the snowman!")
            break

        if mistakes >= len(STAGES) - 1:
            display_game_state(mistakes, secret_word, guessed_letters)
            print(f"Game over. The snowman melted. The word was: {secret_word}")
            break