import random


STAGES = [
   """
     ___ 
    /___\\
    (o o)
    ( : )
    ( : )
   """,
   """
        ___ 
       /___\\
       (o o)
       ( : )
      """,
   """
        ___ 
       /___\\
       (o o)
      """,
   """
     ___ 
    /___\\
   """
]


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




def play_game():
   secret_word = get_random_word()
   print("Welcome to Snowman Meltdown!")
   print("DEBUG: Secret word selected:", secret_word)
   mistakes = 0
   guessed_letters = set()


   while True:
       display_game_state(mistakes, secret_word, guessed_letters)
       guess = input("Guess a letter: ").lower().strip()
       if not guess or len(guess) != 1 or not guess.isalpha():
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


       if mistakes >= len(STAGES) - 1:
           display_game_state(mistakes, secret_word, guessed_letters)
           print(f"Game over. The word was: {secret_word}")
           break
       if all(ch in guessed_letters for ch in secret_word):
           display_game_state(mistakes, secret_word, guessed_letters)
           print("You got it!")
           break




if __name__ == "__main__":
   play_game()
