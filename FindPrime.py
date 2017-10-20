import sys
from colorama import init, Fore, Back, Style


#Finds n number of primes using t threads
#returns a list
def find(n):
    primes = []
    while len(primes) < n:
        primes.append(nextPrime(primes))
        progress(primes, n)
    return primes

#finds the next prime after the last one in the list primes[]
#returns an int
def nextPrime(primes):
    if len(primes) > 0:
        num = primes[len(primes)-1] + 1
        while not isPrime(num, primes):
            num = num + 1
        return num
    else:
        return 2

def isPrime(num, primes):
    for prime in primes:
        if num%prime == 0:
            return False
    Tracker.found_primes.append(num)
    # print(num)
    return True

#prints the percent progress of the program
def progress(primes, n):
    prog = int(( float( len( primes ) ) / n ) * 100)
    if prog > Tracker.lastUpdate:
        
        loading = ""
        for i in range(0,(prog // 2)):
            loading += "#"
        for i in range(0,50 - (prog //2) ):
            loading += " "
        bar = Fore.RED + "[" + Fore.GREEN + loading + Fore.RED + "] " + Fore.YELLOW + str(prog) + "%"
        
        sys.stdout.write("\r" + bar)
        sys.stdout.flush()
        Tracker.lastUpdate = prog

class Tracker:
    lastUpdate = 0
    found_primes = []

init()
x = input("Enter the number of primes to find: ")
find(int(x))
# print('\n')
