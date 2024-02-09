# Do not modify this class
class Node:
    """Node object to be used in DoublyLinkedList"""

    def __init__(self, item, _next=None, _prev=None):
        """initializes new node objects"""
        self.item = item
        self._next = _next
        self._prev = _prev

    def __repr__(self):
        """String representation of Node"""
        return f"Node({self.item})"


class DoublyLinkedList:
    def __init__(self, items=None):
        """Construct a new DLL object"""
        self._head = None
        self._tail = None
        self._len = 0
        self._nodes = dict()  # dictionary of item:node pair.s

        # initialize list w/ items if specified
        if items is not None:
            for item in items:
                self.add_last(item)

    def __len__(self):
        """Returns number of nodes in DLL"""
        return self._len

    # TODO: Modify the 4 methods below to keep `self._nodes` up-to-date
    def add_first(self, item):
        """Adds item to front of dll"""
        # add new node as head
        self._head = Node(item, _next=self._head, _prev=None)
        self._len += 1

        updated_dict = {item, self._head}
        updated_dict.update(item, updated_dict)

        # if that was the first node
        if len(self) == 1:
            self._tail = self._head

        # otherwise, redirect old heads ._tail pointer
        else:
            self._head._next._prev = self._head

    def add_last(self, item):
        """Adds item to end of dll"""
        # add new node as head
        node = Node(item, _next=None, _prev=self._tail)
        self._tail = node
        self._len += 1

        self._tail = self._nodes[item]

        # if that was the first node
        if len(self) == 1:
            self._head = self._tail

        # otherwise, redirect old heads ._tail pointer
        else:
            self._tail._prev._next = self._tail

        self._tail = self._tail._prev

        if node._prev:
            self._nodes[node._prev.item]._next = node

    def remove_first(self):
        """Removes and returns first item"""
        if len(self) == 0:
            raise RuntimeError("cannot remove from empty dll")

        # extract item for later
        item = self._head.item

        # move up head pointer
        self._head = self._head._next
        self._len -= 1

        del self._nodes[self._head]

        # was that the last node?
        if len(self) == 0:
            self._tail = None

        else:
            self._head._prev = None
            self._nodes[self._head.item]._prev = None
        self._nodes.pop(item)

        return item

    def remove_last(self):
        """Removes and returns last item"""
        if len(self) == 0:
            raise RuntimeError("cannot remove from empty dll")

        # extract item for later
        item = self._tail.item

        # move up tail pointer
        self._tail = self._tail._prev
        self._len -= 1

        # was that the last node?
        if len(self) == 0:
            self._head = None

        else:
            self._tail._next = None
            self._nodes[self._head.item]._next = None
        self._nodes.pop(item)

        return item

    # TODO: Add a docstring and implement
    def __contains__(self, item):
        """Returns whether a value is in the DLL"""
        if item in self._nodes:
            return True
        else:
            return False

    # TODO: Add a docstring and implement
    def neighbors(self, item):
        """Returns the items immediately before and after the node with the item"""
        node = self._nodes[item]

        if node._prev:
            previous = node._prev.item
        else:
            previous = None

        if node._next:
            next = node._next.item
        else:
            next = None

        return previous, next

    # TODO: Add a docstring and implement
    def remove_node(self, item):
        """Removes the node containing an item from DLL"""
        if item not in self._nodes:
            raise RuntimeError()  # runtime error
        node = self._nodes[item]

        # Update prev. node w/ next pointer
        if node._prev is not None:
            node._prev._next = node._next
        else:
            self._head = node._next

        # Update next node's prev. pointer
        if node._next is not None:
            node._next._prev = node._prev
        else:
            self._tail = node._prev

        # updating dict. & corresponding length
        del self._nodes[item]
        self._len -= 1
