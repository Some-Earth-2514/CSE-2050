"""
Lecture vids - mod08b
"""
# Map ADT supports at a minimum:
#   * put(key, value) - adds key:value pair
#   * get(key)        - returns value associated with key

# Our mapping object will be composed of a list of "Entry"s


class Entry:
    def __init__(self, key, value):
        self.key = key
        self.value = value


class Mapping:
    def __init__(self):
        self._L = []  # list to hold our items

    def __setitem__(self, key, value):
        # Case 1: key already in mapping
        for entry in self._L:
            if entry.key == key:
                entry.value = value
                return None

        # Case 2: key not already mapping
        self._L.append(Entry(key, value))

    def __getitem__(self, key):
        # Case 1: key in mapping
        for entry in self._L:
            if entry.key == key:
                return entry.value

        # Case 2: key not in mapping
        raise KeyError("key: {} is not in mapping".format(key))


if __name__ == '__main__':
    import time

    # Print a table of times to add an item to a mapping with n items using lists and dicts
    lm = Mapping()
    dm = dict()

    # Print table header
    width = 40
    print("=" * width)
    print("{:<10}{:<10}{:<10}".format("n", "dict map", "list map"))
    print("-" * width)

    # ns = [int(10 ** i) for i in range(7, 0, -1)]
    ns = [10000 * i for i in range(1, 10)]
    n_old = 0
    for n in ns:
        print("{:<10}".format(n), end="")

        # build a dict of n-1 items
        for i in range(n_old, n-1):
            dm[i] = str(i)

        # time how long adding one more item takes
        start = time.time()
        dm[n-1] = str(n-1)
        print("{:<10.3g}".format(time.time() - start), end='')

        # build a list of n-1 items
        for i in range(n_old, n-1):
            lm[i] = str(i)

        # time how long adding one more item takes
        start = time.time()
        lm[n-1] = str(n-1)
        print("{:<10.3g}".format(time.time() - start))

        # keep track of old n to speed up building step
