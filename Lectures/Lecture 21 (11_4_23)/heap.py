class Entry:
    def __init__(self, priority, item):
        self.priority = priority  # (priority, time.time())
        self.item = item

    def __lt__(self, other):
        # this is where you handle tie breaking
        return self.priority < other.priority

    def __repr__(self):
        return f"Entry({self.priority}, {self.item})"


class Heap:
    def __init__(self):
        self._L = []
        self._len = 0

    def __len__(self):
        return len(self._L)

    def add(self, priority, item):
        # append entry to end of list
        # upheap

        new_e = Entry(priority=priority, item=item)

    def upheap(self, idx=None):
        if idx is None:
            idx = len(self) - 1

        # do i have a parent?
        idx_p = self.parent(idx)
        # if so, is the parent smaller?
        if idx_p is None:
            return
        # if so, swap, repeat
        while idx_p is not None and self._L[idx_p] < self._L[idx]:
            # swap items
            self._L[idx_p], self._L[idx] = self._L[idx], self._L[idx_p]
            idx = idx_p
            idx_p = self.parent(idx_p)

    def parent(self, idx):
        """Returns idx of parent"""

    def left(self, idx):
        """Returns idx of left child"""

    def right(self, idx):
        """Returns idx of right child"""
        