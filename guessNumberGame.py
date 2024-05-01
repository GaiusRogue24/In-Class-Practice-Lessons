import random
guess = random.randint(1, 10)
i = 0

while i < 4:
    userInput = int(input("Enter Your Guess: "))
    if guess == userInput:
        print("Congratulations! You guessed the number!")
        break
    elif guess > userInput:
        print("Too low! Try guessing higher.")
    elif guess < userInput:
        print("Too high! Try guessing lower.")
    i += 1
if i == 4:
    print("Game Over")

