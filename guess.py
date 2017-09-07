import random

secret = random.randint(1,10)

for i in range (0,3):
    guess = int(input("Guess a number: "))
    if guess==secret:
        print("You win")
        break
    else:
        print("Wrong")
print("Thanks for playing. Secret number was",7secret)