import random
from ascii import STAGES

WORDS = ["python", "git", "github", "snowman", "meltdown"]

def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]

def display_game_state(mistakes, secret_word, guessed_letters):
    """Renders the current ASCII stage + masked word + metadata."""
    stage_index = min(mistakes, len(STAGES) - 1)
    print(STAGES[stage_index])
    masked = " ".join([ch if ch in guessed_letters else "_" for ch in secret_word])
    print(f"Word: {masked}")
    print(f"Mistakes: {mistakes}/{len(STAGES) - 1}")
    if guessed_letters:
        print("Guessed letters:", " ".join(sorted(guessed_letters)))
    else:
        print("Guessed letters: -")
    print("-" * 30)

def normalize_guess(guess:str) -> str:
    """Normalize and validate a single-letter guess; return '' if invalid."""
    guess = guess.lower().strip()
    if len(guess) != 1 or not guess.isalpha():
        return ""

    return guess

def is_word_resolved(secret_word, guessed_letters) -> bool:
    """Check if all letters of secret_word have been guessed."""
    return all(ch in guessed_letters for ch in secret_word)

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