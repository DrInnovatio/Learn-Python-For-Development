import random

secretNumber = random.randint(0, 6)

count = 0

while count < 3:

    guess = int(input("Guess : "))
    count += 1
    if guess == secretNumber:
        print("You got it!!")
        break

else:
    print("Fail !!")