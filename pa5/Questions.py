import sys

print "\nEnter two numbers, low then high."
low = int(input("low = "))
high = int(input("high = "))
count, guess = 0, 0
plural = ""
letter = ""

while low > high:
    print "\nPlease enter the smaller followed by the larger number."
    low = int(input("low = "))
    high = int(input("high = "))

print "\nThink of a number in the range "+str(low)+" to "+str(high)+"."

def Guess(low, high, count):
    guess = (high + low)/2
    count += 1
    if float(high - low)/2 == 1:
        count -= 1
        print "\nYour number is "+str(guess)+". I found it in "+str(count)+" guesses.\n"
        sys.exit(0)
    return guess, count

guess, count = Guess(low, high, count)

if low == high:
    print "\nYour number is "+str(low)+". I found it in 0 guesses.\n"
    sys.exit(0)

def NotValidInput(guess, count, letter, low, high):
    letter = raw_input ("\nPlease type 'L', 'G' or 'E': ")
    if letter == "E" or letter == "e":
        if count == 1:
            plural = (" guess.")
        else:
            plural = (" guesses.")
        print "\nYour number is "+str(guess)+". I found it in "+str(count)+str(plural)
        print
        sys.exit(0)
    elif letter == "G" or letter == "g":
        low = guess
        high = high
        guess, count = Guess(low, high, count)
        if float(high-guess) < 1:
            print "\nYour answers have not been consistent.\n"
            sys.exit(0)
        UserInput(guess, count, letter, low, high)
    elif letter == "L" or letter == "l":
        low = low
        high = guess
        guess, count = Guess(low, high, count)
        if float(guess-low) < 1:
            print "\nYour answers have not been consistent.\n"
            sys.exit(0)
        UserInput(guess, count, letter, low, high)
    else:
        NotValidInput(guess, count, letter, low, high)

def UserInput(guess, count, letter, low, high):
    print "\nIs your number Less than, Greater than, or Equal to "+str(guess)+"?"
    letter = raw_input ("Type 'L', 'G' or 'E': ")
    if letter == "E" or letter == "e":
        if count == 1:
            plural = (" guess.")
        else:
            plural = (" guesses.")
        print "\nYour number is "+str(guess)+". I found it in "+str(count)+str(plural)
        print
        sys.exit(0)
    elif letter == "G" or letter == "g":
        low = guess
        high = high
        guess, count = Guess(low, high, count)
        if float(high-guess) < 1:
            print "\nYour answers have not been consistent.\n"
            sys.exit(0)
        UserInput(guess, count, letter, low, high)
    elif letter == "L" or letter == "l":
        low = low
        high = guess
        guess, count = Guess(low, high, count)
        if float(guess-low) < 1:
            print "\nYour answers have not been consistent.\n"
            sys.exit(0)
        UserInput(guess, count, letter, low, high)
    else:
        NotValidInput(guess, count, letter, low, high)

UserInput(guess, count, letter, low, high)
