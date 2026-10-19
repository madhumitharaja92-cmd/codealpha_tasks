import random

# Five predefined words
words = ["apple", "tiger", "house", "water", "chair"]


def play_hangman():
    word = random.choice(words)
    guessed_letters = []
    wrong_guesses = 0
    max_wrong_guesses = 6

    print("\n==============================")
    print("       WELCOME TO HANGMAN")
    print("==============================")
    print("Guess the hidden word!")
    print("You have 6 incorrect guesses.")

    while wrong_guesses < max_wrong_guesses:
        # Display the word
        display_word = ""
        for letter in word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "

        print("\nWord:", display_word)
        print("Wrong guesses:", wrong_guesses)
        print("Letters guessed:", guessed_letters)

        # Check whether the word is complete
        if all(letter in guessed_letters for letter in word):
            print("\nCongratulations! You won!")
            print("The word was:", word)
            return

        # Get one letter from the player
        guess = input("Enter one letter: ").strip().lower()

        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter only ONE alphabet letter.")
            continue

        # Check repeated guesses
        if guess in guessed_letters:
            print("You already guessed that letter!")
            continue

        guessed_letters.append(guess)

        # Check the guess
        if guess in word:
            print("Correct guess!")
        else:
            wrong_guesses += 1
            print("Wrong guess!")

    print("\nGame Over!")
    print("The correct word was:", word)


if __name__ == "__main__":
    play_hangman()
