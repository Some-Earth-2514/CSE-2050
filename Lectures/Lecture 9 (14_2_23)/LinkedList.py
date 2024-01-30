class LLNode:
    def __init__(self, item, _next):
        self.item = item
        self.next = _next

    def __repr__(self):
        return f"LLNode({self.item}"


class LinkedList:
    def __init__(self, items=None):
        # initializing an empty LL
        self._head = None
        self._tail = None
        self._len = 0

        if items is not None:
            for item in items:
                self.add_last(item)  # update head, tail, and len

    def add_last(self, item):
        # create node
        new_node = LLNode(item, _next=None)  # O(1)

        # update old tail node's next
        if len(self) > 0:  # O(1)
            self._tail._next = new_node

        else:
            self._head = new_node  # first node in LL

        # update my tai pointer
        self._tail = new_node  # O(1)

        self._len += 1

    def remove_last(self):
        if len(self) == 0:
            raise RuntimeError("Cannot remove from empty LL")

        item = self._tail.item  # 1

        # update penultimate node's ._next
        penultimate = self._head  # 1

        # when len(self) === 1:
        # head-----v
        #        LLNode-->None
        # tail-----^

        # O(n)
        if len(self) > 1:  # 1
            while penultimate._next._next is not None:  # n - 1
                penultimate = penultimate._next  # 1

        penultimate._next = None  # 1

        self._tail = penultimate  # 1

        self._len -= 1  # c53 1 (arithm)

        return item  # 1
