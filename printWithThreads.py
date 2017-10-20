from threading import Thread
import os

class db:
    nums = [1,2,3,4,5,6,7,8,9]
    result = []
    lastIndex = 0

def runner():
    '''
    spawns TRHEADS threads
    each take turns taking a number out of the db
    and printing it, making sure they print the right number
    '''

    THREADS = 8

    for i in range(0, THREADS):
        t = Thread(target = printer)
        t.start()
    
def printer():
    while db.lastIndex < len(db.nums):
        i = db.nums[db.lastIndex]
        li = db.lastIndex
        db.lastIndex += 1
        db.result.append(i)
        print(i)
