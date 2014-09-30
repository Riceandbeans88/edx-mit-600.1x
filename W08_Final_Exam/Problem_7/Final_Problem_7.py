# coding=utf-8
#PROBLEM 7-1
class Frob(object):
    def __init__(self, name):
        self.name = name
        self.before = None
        self.after = None
    def setBefore(self, before):
        # example: a.setBefore(b) sets b before a
        self.before = before
    def setAfter(self, after):
        # example: a.setAfter(b) sets b after a
        self.after = after
    def getBefore(self):
        return self.before
    def getAfter(self):
        return self.after
    def myName(self):
        return self.name



#Example Output
'''
eric = Frob('eric')
andrew = Frob('andrew')
ruth = Frob('ruth')
fred = Frob('fred')
martha = Frob('martha')

insert(eric, andrew)
insert(eric, ruth)
insert(eric, fred)
insert(ruth, martha)
'''


def insert(atMe, newFrob):
    '''
    atMe: a Frob that is part of a doubly linked list
    newFrob:  a Frob with no links 
    Procedure inserts newFrob into the linked list that atMe is a part of.
    '''
    # Your Code Here
    #Hints What 2 cases should you think about?
    #Whether the newFrob should be before or after atMe.



#PROBLEM 7-2
def findFront(start):
    """
    start: a Frob that is part of a doubly linked list
    returns: the Frob at the beginning of the linked list
    """
    # Your Code Here
