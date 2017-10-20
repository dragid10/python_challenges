'''
Copyright Reese Wells, 2017
'''
from LinkedList import BinarySearchTree

class PrefixTree:
    '''
    A prefix tree implementation
    '''
    def __init__(self):
        self._children = []
        self._data = None

    def add(self, data):
        '''
        Adds a new letter to the tree

        rtype : boolean

        returns True if data was added
        returns False if data was already there
        '''
        if not self.contains(data):
            newChild = PrefixTree()
            newChild._data = data
            self._children.append(newChild)
            return True
        else:
            return False

    def contains(self, data):
        '''
        Checks if the given node has a child that matches data

        rtype : boolean

        returns True if one of the children's data matches
        returns False if none of the children's data matches
        '''
        for child in self._children:
            if child._data == data:
                return True
        else:
            return False

    def getContainer(self, data):
        '''
        Similar to contains, but instaed of returning a boolean it returns
        the PrefixTree of the found data

        rtype : PrefixTree()

        returns PrefixTree() if one of the children's data matches
        returns None if none of the children's data matches
        '''
        for child in self._children:
            if child._data == data:
                return child
        else:
            return None

    def addWord(self, word):
        '''
        adds a word to the tree by recursively calling add()

        rtype : boolean

        returns True if the word was added
        returns False if the tree already contained the word

        NOTE: returns true if given an empty string
        '''
        if self.containsWord(word):
            return False
        if len(word) == 0:
            self.add('.')
            return True
        else:
            self.add(word[0])
            return self.getContainer(word[0]).addWord(word[1:])

    def containsWord(self, word):
        '''
        Checks if the tree contains the given word by calling contains()
        recursively and checking each letter

        rtype : boolean

        returns True if the tree contains the word
        returns False if the tree does not contain the word
        '''
        # if the current level does not contains the first letter
        if len(word) == 0:
            return self.contains(".")
        if not self.contains(word[0]):
            return False
        else:
            return self.getContainer(word[0]).containsWord(word[1:])

def test():
    # test making the tree
    p = PrefixTree()
    print ("adding 'a': " + str(p.add('a')))
    print ("adding 'b': " + str(p.add('b')))
    print ("adding 'a': " + str(p.add('a')))
    print ("contains 'a': " + str(p.contains('a')))
    print ("temp = p.getContainer 'a'")
    temp = p.getContainer('a')

    # test getContainer
    print ("temp.add('a'): " + str(temp.add('a')))
    print ("temp.add('a'): " + str(temp.add('a')))
    print ("temp.contains('a'): " + str(temp.contains('a')))

    # test containsWord
    print ("p.containsWord('aa'): " + str(p.containsWord('aa')))
    print ("p.containsWord('ab'): " + str(p.containsWord('ab')))
    print ("p.containsWord('abcd'): " + str(p.containsWord('abcd')))
    print ("p.containsWord('d'): " + str(p.containsWord('d')))

    # test addWord
    print ("p = PrefixTree(): ")
    p = PrefixTree()
    print ("adding 'hello': " + str(p.addWord('hello')))
    print ("adding 'hello': " + str(p.addWord('hello')))
    print ("adding 'world': " + str(p.addWord('world')))
    print ("adding 'python': " + str(p.addWord('python')))
    print ("adding 'java': " + str(p.addWord('java')))
    print ("adding 'word': " + str(p.addWord('word')))

    # test containsWord
    print ("p.containsWord('hello'): " + str(p.containsWord('hello')))
    print ("p.containsWord('hel'): " + str(p.containsWord('hel')))
    print ("p.containsWord('world'): " + str(p.containsWord('world')))
    print ("p.containsWord('w'): " + str(p.containsWord('w')))
    print ("p.containsWord('python'): " + str(p.containsWord('python')))
    print ("p.containsWord('pythone'): " + str(p.containsWord('pythone')))
    print ("p.containsWord('java'): " + str(p.containsWord('java')))
    print ("p.containsWord(''): " + str(p.containsWord('')))
    print ("p.containsWord('word'): " + str(p.containsWord('word')))

def testDictionary():
    '''
    Adds all the words in the dictionary from the file "words.txt"

    rtype : PrefixTree()
    '''
    f = open('words.txt', 'r')
    words = []
    for line in f:
        words.append(line.strip())

    # first get a line count to know how many words we've added at any give time
    lineCount = len(words)

    # now add the words, spitting out percentages on occasion
    currentLine = 0
    currentProgress = 0
    dictionaryTree = PrefixTree()
    print()
    print("Adding words to the Prefix Tree")

    for line in words:

        # get our current progress through the words
        percentDone = int((currentLine / lineCount) * 100)
        if percentDone > currentProgress:
            currentProgress = percentDone
            print("finished adding " + str(currentProgress) + "% of words to the Prefix Tree")

        # add the next word
        dictionaryTree.addWord(line.strip())

        #increment currentLine
        currentLine = currentLine + 1

    # create a binary search tree to hold the same data
    currentLine = 0
    currentProgress = 0
    binaryTree = BinarySearchTree()
    print()
    print("Adding words to the Binary Tree")
    binaryTree.addList(words)

    return [dictionaryTree, binaryTree]













    
