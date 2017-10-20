from threading import Thread
import pickle

def threadTest():
    t = Thread(target = saveAndLoad)
    t.start()
    print('should be printed after "hello"')

def saveAndLoad():
    p = Person('New','Person',23,'F')
    b = p.toBytes()
    p.first_name = 'Newer'
    p.last_name = 'Name'
    p.save()
    print('\nhello')

class Person:
    def __init__(self, first_name, last_name, age, sex):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.sex = sex

    def toBytes(self):
        return pickle.dumps(self)

    def save(self):
        f = open(self.first_name + "_" + self.last_name, 'wb')
        pickle.dump(self, f)
        f.close()

    def load(first_name, last_name):
        f = open(first_name + "_" + last_name, 'rb')
        return pickle.load(f)
