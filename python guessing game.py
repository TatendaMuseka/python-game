import random

numGames = int(input("How many games would you like to play? -->"))
score = 0
for i in range(0, numGames):
    print("Game start!")
    hiddenNumber = random.randint(1, 5)
    userGuess = 0
    chance = 3
    wasted = 3

    while userGuess != hiddenNumber and chance > 0:
        userGuess = int(input("Guess a number between 1 to 5: "))
        if userGuess == hiddenNumber:
            print("That's right!")
            score += 10
            chance -= 3
        elif wasted > 0:
            wasted -= 1
            print("You missed it")
            print("You have", wasted, "chances left.")
            chance -= 1
print("Your Score:", score)
