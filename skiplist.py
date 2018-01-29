import pdb
import random

class SkipNode:
    def __init__(self, data, height):
        self.data = data
        height += 1
        self.front = [None] * height

    def __str__(self):
        front_s = []
        for f in self.front:
            if f:
                front_s.append('{}'.format(f.data))
            else:
                front_s.append('/')
        s = '{}, [{}]'.format(self.data, ', '.join(front_s))
        return s

    def __repr__(self):
        return self.__str__()
    
    def height(self):
        return len(self.front)-1

    def add_levels(self, n):
        self.front.extend([None]*n)

class SkipList:
    def __init__(self, limit=100):
        self.sentinel = SkipNode(None, 0)
        self.limit = limit

    def __str__(self):
        lst = []
        node = self.sentinel.front[0]
        while node:
            lst.append('{}'.format(node))
            node = node.front[0]
        return '-> '.join(lst)
    
    def __repr__(self):
        return self.__str__()
        
    def height(self):
        return self.sentinel.height()
        
    def find_predecessor(self, x):
        pdb.set_trace()
        node = self.sentinel
        h = self.sentinel.height()
        stack = [None] * (h+1)
        while h >= 0:
            front = node.front[h]
            while front and front.data < x:
                node = front
                front = node.front[h]
            stack[h] = node
            h -= 1
        return (node, stack)

    def find(self, x):
        pred, _ = find_predecessor(x)
        return pred.front[0].data
    
    def add(self, x):
        # pdb.set_trace()
        add_me = SkipNode(x, random.randint(0,self.limit))
        added_h = add_me.height()
        if added_h > self.height():
            self.sentinel.add_levels(added_h-self.height())
        pred, stack = self.find_predecessor(x)
        if pred.front[0] and pred.front[0].data == x:
            return False
        for i in range(added_h+1):
            add_me.front[i] = stack[i].front[i]
            stack[i].front[i] = add_me
        return True
