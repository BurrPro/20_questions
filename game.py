import random
answer = random.randint(1, 1000)
guess = int(input("Guess a number between 1 and 1000: "))
tries = 0

while guess != answer and tries < 20:
    if guess < answer:
        print("Try again, the correct number is higher.")
        guess = int(input("Guess a number between 1 and 1000: "))
    elif guess > answer:
        print("Try again, the correct number is lower.")
        guess = int(input("Guess a number between 1 and 1000:"))

print(
    "You guessed the number correctly! The correct number was %s, you guessed this in %d tries!"
    % (answer, tries)
)
