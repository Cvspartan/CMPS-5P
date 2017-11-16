import random, sys

number = random.randint(1,10)

print("\nI'm thinking of an integer in the range 1 to 10. You have three guesses.\n")

fg = int(input("Enter your first guess: "))
if fg < number:
    print("Your guess is too low.\n")
elif fg > number:
    print("Your guess is too high.\n")
else:
    print("You win!")
    print
    sys.exit(0)

sg = int(input("Enter your second guess: "))
if sg < number:
    print("Your guess is too low.\n")
elif sg > number:
    print("Your guess is too high.\n")
else:
    print("You win!")
    print
    sys.exit(0)

tg = int(input("Enter your third guess: "))
if tg < number:
    print("Your guess is too low.\n")
    print("You lose. The number was "+str(number)+".")
elif tg > number:
    print("Your guess is too high.\n")
    print("You lose. The number was "+str(number)+".")
else:
    print("You win!")

print
