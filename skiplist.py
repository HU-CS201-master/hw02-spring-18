import random

class Skipnode:
    def __init__(self, data, height):
        '''Initializes node with data and (height+1) front pointers.
        '''
        pass
    
    def __str__(self):
        '''Returns a string representation of an object for printing.
        '''
        pass
    
    def __repr__(self):
        '''Returns a string representation of an object for interactive
        mode.
        '''
        return self.__str__()
    
    def height(self):
        '''Returns the height of this node.
        '''
        pass

    def add_levels(self, n):
        '''Adds n front pointers.
        '''
        pass

class Skiplist:
    def __init__(self, limit=100):
        '''Initializes sentinel, height limit, and size.
        '''
        pass
        
    def __str__(self):
        '''Returns a string representation of an object for printing.
        '''
        pass
    
    def __repr__(self):
        '''Returns a string representation of an object for interactive
        mode.
        '''
        return self.__str__()
        
    def height(self):
        '''Returns the height of the skiplist.
        '''
        pass
        
    def find_predecessor(self, x):
        '''Returns (predecessor_node, stack).
        '''
        pass
    
    def find(self, x):
        '''Returns x, its successor, or None, in that order.
        '''
        pass
    
    def add(self, x):
        '''Adds x to the skiplist and returns True; does not add and
        returns False if x is already an element.
        '''
        pass
    
    def remove(self, x):
        '''Remoces x from the skiplist and returns True; does not remove
        and returns False if x is not an element.
        '''
        pass
    
    def truncate(self, i):
        # As described in Exercise 4.11
        pass

    def absorb(self, l2):
        # As described in Exercise 4.12
        pass
