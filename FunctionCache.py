import numpy as np

class FunctionCache:
    def __init__(self):
        self.cache = {}

    def store(self, key, value):
        self.cache[key] = value

    def smartStore(self, value, *argv):
        self.cache[np.uint64(hash("".join(map(str, argv))))] = value

    def get(self, key):
        return self.cache[key]

    def smartGet(self, *argv):
        return self.cache[np.uint64(hash("".join(map(str, argv))))] 

    def safeGet(self, key):
        if key in self.cache:
            return self.cache[key]