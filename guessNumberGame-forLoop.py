import random
guess = random.randint(1, 10)
print(guess)

for i in range(4):
    userInput = int(input("Enter Your Guess: "))
    if guess == userInput:
        print("Congratulations! You guessed the number!")
        break
    elif guess < userInput:
        print("Too high! Try guessing lower.")
    elif guess > userInput:
        print("Too low! Try guessing higher.")
else:
    print("Game Over")

