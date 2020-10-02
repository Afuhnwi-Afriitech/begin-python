import random

random_number = random.randint(1, 10)
print(random_number)
rand_number = int(input("Enter a random number: "))
guess = 1
while guess < 3:
    if rand_number == random_number:
        print("You guessed correctly")
        break
    elif rand_number == 0:
        break
    elif rand_number < random_number:
        rand_number = int(input("Guess again! but this time, with a higher number: "))
    elif rand_number > random_number:
        rand_number = int(input("Guess again with a lower number"))
    guess += 1
