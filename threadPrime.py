from threading import Thread
import os, sys

class db:
    lastTested = 1 # the last prime number tested
    found_primes = [] # the list of found primes
    target = 0
    
def runner(target, threads):
    '''
    spawns TRHEADS threads
    each take turns taking a number out of the db
    and printing it, making sure they print the right number
    '''

    THREADS = threads
    db.target = target
    
    for i in range(0, THREADS):
        t = Thread(target = finder)
        t.start()

    t = Thread(target = printer)
    t.start()

def printer():
    done = False

    while not done:
        done = len(db.found_primes) >= db.target

    sys.stdout.write("Done.\n")
    sys.stdout.flush()

def finder():
    while len(db.found_primes) < db.target:
        test = db.lastTested + 1
        db.lastTested += 1

        isPrime(test)
        
def isPrime(n):
    previousPrimes = db.found_primes
    for prime in previousPrimes:
        if n % prime == 0:
            return False
    db.found_primes.append(n)
    return True

if __name__ == '__main__':
    runner(100000, 4)
