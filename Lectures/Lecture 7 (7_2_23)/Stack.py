import time


class Stack:
    """List 'wrapper'"""

    def __init__(self):
        self._L = []  # consider it a private variable with the _ in front of the variable name
        # attributes that start with 1 leading underscore are "private"
        # should only be accessed within this class

    def push(self, item):
        self._L.append(item)

    def pop(self):
        return self._L.pop()


"""
s = Stack()
s._L.append(4) # no no
"""


class StackSet:
    """List 'wrapper'"""

    def __init__(self):
        self._S = set()  # consider it a private variable with the _ in front of the variable name
        # attributes that start with 1 leading underscore are "private"
        # should only be accessed within this class

    def push(self, item):
        new_item = (time.time(), item)
        self._S.add(new_item)
        time.sleep(0.01)

    def pop(self):
        # find the most recent time stamp
        t_max = 0
        for item_tup in self._S:
            print(f"item_tup = {item_tup}")
            if item_tup[0] > t_max:
                t_max = item_tup[0]
                item_tup_max = item_tup

        self._S.remove(item_tup_max)
        return item_tup_max[1]


class Queue:
    def __init__(self):
        self._L = []  # composition - my queue *has a* list

    def enqueue(self, item):
        # add an item to end of queue
        self._L.append(item)

    def dequeue(self):
        # remove and return an item from beginning of queue
        return self._L.pop(0)
