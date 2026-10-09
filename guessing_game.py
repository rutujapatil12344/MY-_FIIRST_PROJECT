import random

number = random.randint(1, 10)
guess = int(input("1 se 10 ke beech number guess karo: "))

if guess == number:
    print("Wah! Sahi jawab!")
else:
    print("Galat! Sahi number tha", number)
