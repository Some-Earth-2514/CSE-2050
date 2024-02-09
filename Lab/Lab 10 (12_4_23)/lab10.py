# This file empty on purpose - add the correct classes/methods below

class Entry:
    def __init__(self, item, priority):
        self.item = item
        self.priority = priority

    def __lt__(self, other):
        if self.priority < other.priority:
            return True
        return False

    def __eq__(self, other):
        if self.priority == other.priority and self.item == other.item:
            return True
        return False


class PQ_UL:
    def __init__(self):
        self._L = []

    def __len__(self):
        return len(self._L)

    def insert(self, item, priority):
        self._L.append(Entry(item, priority))

    def find_min(self):
        return min(self._L)

    def remove_min(self):
        entry = min(self._L)
        self._L.remove(entry)
        return entry


class PQ_OL:
    def __init__(self):
        self._L = []

    def __len__(self):
        return len(self._L)

    def insert(self, item, priority):
        self._L.append(Entry(item, priority))
        self._L.sort(reverse=True)

    def find_min(self):
        return min(self._L)

    def remove_min(self):
        entry = min(self._L)
        self._L.remove(entry)
        return entry
