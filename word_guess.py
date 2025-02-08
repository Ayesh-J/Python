import random

name = input("Enter your name: ")

print("Good Luck! " + name)

words = ['milf', 'anal', 'time', 'dilkush briyani', 'pussy', 'cottons', 'salman khan', 'kanban']

word = random.choice(words)

print("Guess the characters in the word:")
guesses = ''
turns = 12

while turns > 0:
    failed = 0
    for char in word:
        if char in guesses:
            print(char, end=" ")
        else:
            print("_", end=" ")
            failed += 1  # Corrected this line

    print()  # Move to the next line after printing the word state

    if failed == 0:
        print("You win!")
        print("The word is:", word)
        break  # Exit the loop if the player has won

    guess = input("Guess a character: ")
    guesses += guess

    if guess not in word:
        turns -= 1
        print("Wrong guess!")
        print("You have", turns, 'more guesses')

        if turns == 0:
            print("You Lose! The word was:", word)