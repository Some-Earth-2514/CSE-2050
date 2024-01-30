class Node:
    def __init__(self, item, _next=None):
        self.item = item
        self._next = _next


class LinkedList:
    def __init__(self):
        self._head = None
        self._tail = None
        self._len = 0

    def __len__(self):
        return self._len

    def add_first(self, item):
        # edge case - this is the first node I'm adding
        # general case - 1 or more nodes in LL already

        new_node = Node(item, _next=self._head)
        self._head = new_node
        self._len += 1

    def add_last(self):
        pass

    def remove_first(self):
        # edge case - this is the last node removed

        if len(self) == 1:
            self._tail = None
            """
            item = self._head.item
            self._head = None
            self._tail = None
            self._len -= 1
            return item
            """

        # general case

        item = self._head.item

        self._head = self._head._next

        self._len -= 1

        return item

    def remove_last(self):
        pass
