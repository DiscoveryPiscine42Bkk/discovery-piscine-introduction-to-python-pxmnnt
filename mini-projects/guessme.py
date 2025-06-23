import random

secret_number = random.randint(1, 100)

print("Welcome to the Guess the Number game!\n")
print("I have generated a secret number between 1 and 100. You have 5 guesses.\n")

attempts = 5
highest = 100
lowest = 1

while attempts > 0:
    print(f"Attempts left: {attempts}")
    guess = int(input("Enter your guess: "))
    if guess != secret_number:
        if guess < secret_number:
            lowest = guess + 1
            print(f"Your guess is not correct. The secret number is between {lowest} and {highest}.")
        else:
            highest = guess - 1
            print(f"Your guess is not correct. The secret number is between {lowest} and {highest}.")
        attempts -= 1
    else:
        print("Correct! You've guessed the secret number!")
        break

if attempts == 0:
    print(f"Sorry, you've run out of attempts. The secret number was {secret_number}.")
    
print("Thank you for playing!")