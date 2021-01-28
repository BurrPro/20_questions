import random
answer = random.randint(1, 100)
guess = int(input("Guess a number between 1 and 100: "))
tries = 0

while guess != answer and tries < 10:
    if guess < answer:
        print("Try again, the correct number is higher.")
        guess = int(input("Guess a number between 1 and 100: "))
    elif guess > answer:
        print("Try again, the correct number is lower.")
        guess = int(input("Guess a number between 1 and 100:"))

print(
    "You guessed the number correctly! The correct number was %s, you guessed this in %d tries!"
    % (answer, tries)
)
