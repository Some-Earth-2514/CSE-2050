"""
Lecture vids - mod08b
"""
# Map ADT supports at a minimum:
#   * put(key, value) - adds key:value pair
#   * get(key)        - returns value associated with key


class Entry:
    def __init__(self, key, value):
        self.key = key
        self.value = value


class Mapping:
    def __init__(self):
        self._L = []

    def __setitem__(self, key, value):
        for entry in self._L:
            if entry.key == key:
                entry.value = value
                return None

        self._L.append(Entry(key, value))

    def __getitem__(self, key):
        for entry in self._L:
            if entry.key == key:
                return entry.value
        raise KeyError("key: {} is not in mapping".format(key))


if __name__ == '__main__':
    m = Mapping()
    n = 100
    for i in range(n):  # testing __put__()
        m[i] = str(i)

    for i in range(n):  # testing __get__()
        assert m[i] == str(i)
