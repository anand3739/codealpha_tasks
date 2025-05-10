import random

# Predefined list of words
word_list = ["python", "hangman", "developer", "programming", "algorithm"]

def choose_word():
    return random.choice(word_list)

def display_word(word, guessed_letters):
    return "".join(letter if letter in guessed_letters else "_" for letter in word)

def hangman():
    word = choose_word()
    guessed_letters = set()
    attempts = 6

    print("Welcome to Hangman!")
    
    while attempts > 0:
        print("\nWord:", display_word(word, guessed_letters))
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print("Good guess!")
        else:
            attempts -= 1
            print(f"Wrong guess! {attempts} attempts left.")

        if set(word).issubset(guessed_letters):
            print("\nCongratulations! You've guessed the word:", word)
            break
    else:
        print("\nGame Over! The word was:", word)

# Start the game
hangman()
