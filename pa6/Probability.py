import random

rng = random.Random()

def throwDice(m, k):
    rolls = []
    for i in range(m):
        throw = rng.randrange(1, k+1)
        rolls.append(throw)
    return rolls

m = int(input("\nEnter the number of dice: "))
while m < 1:
    print "The number of dice must be at least 1"
    m = int(input("Please enter the number of dice: "))

k = int(input("\nEnter the number of sides on each die: "))
while k < 2:
    print "The number of sides on each die must be at least 2"
    k = int(input("Please enter the number of sides on each die: "))

trials = int(input("\nEnter the number of trials to perform: "))
while trials < 1:
    print "The number of trials must be at least 1"
    trials = int(input("Please enter the number of trials to perform: "))

possibleSums = (m*k)+1
          
frequency = possibleSums*[0]
for i in range(trials):
    rolls = throwDice(m, k)
    frequency[sum(rolls)] += 1

relativeFrequency = [i/float(trials) for i in frequency]
expProb = [i * 100 for i in relativeFrequency]

print("\n{0:<10}{1:<15}{2:<25}{3:<10}".format("Sum", "Frequency", "Relative Frequency", "Experimental Probability"))
print 80*"-"
table = "{0:<13}{1:<15}{2:<30.5f}{3:<6.2f}{4:<10}"
for i in range(m, len(frequency)):
    print(table.format(i, frequency[i], relativeFrequency[i], expProb[i],"%"))
print
