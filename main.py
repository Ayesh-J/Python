import random

print("Hi! Welcome to the game, This is the number guessing game. You have got 7 chances to guess the number correctly")

number_to_guess = random.randrange(100)

chances = 7

guess_counter = 0

while guess_counter < chances:
    guess_counter += 1
    my_guess = int(input("Please enter your guess:"))

    if my_guess == number_to_guess:
        print(f'the number is {number_to_guess} and you found it right !! in {guess_counter} attempts')
        break

    elif guess_counter >= chances and my_guess != number_to_guess:
        print(f'Oops Sorry The number is {number_to_guess} better luck next time')

    elif my_guess < number_to_guess:
        print(f'your guess is too low, try again')

    elif my_guess > number_to_guess:
        print(f'your guess is too high, try again')