import sys

number = int(input("\nEnter the number of Primes to compute: "))

if number == 1:
    print("The first prime is 2")
    sys.exit(0)

m = 3
PrimeList = [2]

def isPrime(m, L):
    for L in PrimeList:
        if m < L**2:
            PrimeList.append(m)
            return m
        if m%L == 0:
            return m

isPrime(m, PrimeList)

while (len(PrimeList) != number):
    m += 1
    isPrime(m, PrimeList)

print("\nThe first "+str(number)+" primes are:")
for i in range(len(PrimeList)/10+1):
    print " ".join(map(str,PrimeList[i*10:(i+1)*10]))
