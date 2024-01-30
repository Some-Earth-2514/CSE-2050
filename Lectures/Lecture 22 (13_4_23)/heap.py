class Entry:
    def __init__(self, item, priority):
        self.item = item
        self.priority = priority

    def __lt__(self, other):
        return self.priority < other.priority

    def __repr__(self):
        return f"Entry(item={self.item}, priority={self.priority})"


class Heap:
    def __init__(self):
        self._L = []

    def __len__(self):
        return len(self._L)

    def _i_parent(self, idx):
        """returns index of parent of idx"""
        return (idx - 1) // 2 if (idx - 1) // 2 >= 0 else None

    def _i_left(self, idx):
        """left child"""
        il = idx * 2 + 1
        return il if il < len(self) else None

    def _i_right(self, idx):
        """right child"""
        ir = idx * 2 + 2
        return ir if ir < len(self) else None

    def insert(self, item, priority):
        """adds item w/ given priority to heap"""
        # append entry to list
        # upheap until balanced

        new_e = Entry(item=item, priority=priority)
        self._L.append(new_e)
        self._upheap(len(self) - 1)

    def _upheap(self, idx):
        """upheaps item at idx"""
        # find parent index
        i_p = self._i_parent(idx)

        # while parent exists and parent is bigger: swap
        while i_p is not None and self._L[i_p] > self._L[idx]:
            # swap them
            self._L[i_p], self._L[idx] = self._L[idx], self._L[i_p]
            # update vars for next loop
            idx = i_p
            i_p = self._i_parent(idx)

    def peek(self):
        """returns (but does not remove) item with minimum priority"""
        return self._L[0].item

    def remove_min(self):
        """removes and returns item with minimum priority"""
        # extract root to temp variable
        # pop last item, move to root
        # downheap root
        min_item = self._L[0].item
        # edge case - only 1 entry in heap
        if len(self) == 1:
            self._L.pop()
            return min_item

        self._L[0] = self._L.pop()
        self._downheap(idx=0)

        return min_item

    def _find_min_child(self, idx):
        """returns idx of minimum child if it exists, otherwise None"""
        il = self._i_left(idx)
        ir = self._i_right(idx)

        # handles 0 and 1 child cases
        if ir is None:
            return il
        else:
            return il if self._L[il] < self._L[ir] else ir

    def _downheap(self, idx):
        """downheaps item at idx"""
        # swap w/ minimum child until (i) end of tree or (ii) both children are bigger
        i_min = self._find_min_child(idx)

        # if i_min and ...
        while i_min is not None and self._L[i_min] < self._L[idx]:
            self._L[i_min], self._L[idx] = self._L[idx], self._L[i_min]
            # update variables for next loop
            idx = i_min
            i_min = self._find_min_child(idx)


if __name__ == '__main__':
    n = 10
    hp = Heap()
    for i in range(n):
        hp.insert(str(i), i)
        assert hp.peek() == str(0)

    for i in range(n):
        assert hp.peek() == str(i)
        assert hp.remove_min() == str(i)

    print("all done")
