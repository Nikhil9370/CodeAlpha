import random

word_list = ["apple", "grape", "mango", "peach", "berry"]


secret_word = random.choice(word_list)


guessed_letters = []
incorrect_guesses = 0
max_attempts = 6


display_word = ["_" for _ in secret_word]

print("Welcome to Hangman!")
print("Guess the word (fruit name). You have 6 wrong attempts.\n")


while incorrect_guesses < max_attempts and "_" in display_word:
    print("Word:", " ".join(display_word))
    guess = input("Enter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single alphabet letter.\n")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.\n")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:
        for i in range(len(secret_word)):
            if secret_word[i] == guess:
                display_word[i] = guess
        print("Good guess!\n")
    else:
        incorrect_guesses += 1
        print(f"Wrong guess! Attempts left: {max_attempts - incorrect_guesses}\n")


if "_" not in display_word:
    print("Congratulations! You guessed the word:", secret_word)
else:
    print("Game Over! The word was:", secret_word)
