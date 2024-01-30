class Entry:
    def __init__(self, key, value):
        """Initializes a new entry w/ key and value"""
        self.key = key
        self.value = value

    def __repr__(self):
        """String representation of entry"""
        return f"Entry(key={self.key}, value={self.value})"


class ListMapping:
    def __init__(self):
        """Add data structure to store entries"""
        self._L = []  # empty list to store entire key of __init__

    def __setitem__(self, k, v):
        """Add key:value pair to Mapping, or updated value if key already in mapping"""
        new_entry = Entry(k, v)  # new entry to add to mapping
        for e in self._L:
            if e.key == k:
                e.value = v  # update value
                return

        self._L.append(new_entry)

    def __getitem__(self, k):
        """Return value associated with key. Raise a KeyError if key is not in mapping"""
        for e in self._L:
            if e.key == k:
                return e.value
        raise KeyError(f"key {k} not found in ListMapping")


class HashMapping:
    def __init__(self):
        self.n_buckets = 8  # initial size, want this to be a power of 2
        self.L = [[] for i in range(self.n_buckets)]  # list of empty buckets
        self._len = 0  # number of items in set

    def __len__(self):
        return self._len

    def find_bucket(self, key):
        return hash(key) % self.n_buckets

    def __setitem__(self, key, value):
        # 1) find where the item should be
        idx = self.find_bucket(key)

        # 2) scan that bucket, update the k:v pair if you find it
        for entry in self._L[idx]:
            if entry.key == key:
                entry.value = value
                return

        # 3) if not, add to the end of the bucket
        self._L[idx].append(Entry(key, value))
        self._len += 1

        # 4) if i have too many items, REHASH
