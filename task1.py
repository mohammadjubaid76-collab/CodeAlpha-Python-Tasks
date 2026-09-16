import random

WORDS = ["python", "laptop", "coffee", "orange", "school"]

MAX_WRONG = 6


def get_display_word(secret, guessed_letters):
    """Return the word with unguessed letters hidden as underscores."""
    display = ""
    for letter in secret:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()


def get_guess(guessed_letters):
    """Ask the user for a single new letter and validate it."""
    while True:
        guess = input("Guess a letter: ").lower().strip()

        if len(guess) != 1:
            print("Please enter exactly one letter.")
        elif not guess.isalpha():
            print("Letters only - no numbers or symbols.")
        elif guess in guessed_letters:
            print(f"You already guessed '{guess}'. Try a different letter.")
        else:
            return guess


def play():
    secret = random.choice(WORDS)
    guessed_letters = []      # every letter the player has tried
    wrong_guesses = []        # only the incorrect ones
    wrong_count = 0

    print("=" * 40)
    print("        HANGMAN - CodeAlpha Task")
    print("=" * 40)
    print(f"The word has {len(secret)} letters.")
    print(f"You are allowed {MAX_WRONG} wrong guesses.\n")

    while wrong_count < MAX_WRONG:
        print("Word   :", get_display_word(secret, guessed_letters))
        print("Wrong  :", ", ".join(wrong_guesses) if wrong_guesses else "none")
        print(f"Left   : {MAX_WRONG - wrong_count} wrong guess(es)\n")

        guess = get_guess(guessed_letters)
        guessed_letters.append(guess)

        if guess in secret:
            print(f"Correct! '{guess}' is in the word.\n")
        else:
            wrong_count += 1
            wrong_guesses.append(guess)
            print(f"Wrong! '{guess}' is not in the word.\n")

        # Win check: every letter of the secret has been guessed
        if all(letter in guessed_letters for letter in secret):
            print("=" * 40)
            print(f"YOU WIN! The word was '{secret}'.")
            print(f"You finished with {wrong_count} wrong guess(es).")
            print("=" * 40)
            return

    # Loop ended because wrong_count reached MAX_WRONG
    print("=" * 40)
    print("GAME OVER - you ran out of guesses.")
    print(f"The word was '{secret}'.")
    print("=" * 40)


def main():
    while True:
        play()
        again = input("\nPlay again? (y/n): ").lower().strip()
        if again != "y":
            print("Thanks for playing!")
            break
        print()


if __name__ == "__main__":
    main()