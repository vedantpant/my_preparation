import random

class RandomizedSet:

    def __init__(self):
        self.numMap = {}
        self.numList = []

    def insert(self, val):
        if val in self.numMap:
            return False
        self.numMap[val] = len(self.numList)
        self.numList.append(val)

        return True

    def remove(self, val):
        if val not in self.numMap:
            return False
        index = self.numMap[val]
        last_element = self.numList[-1]
        self.numList[index] = last_element
        self.numList.pop()
        self.numMap[last_element] = index
        del self.numMap[val]
        return True

    def getRandom(self):
        return random.choice(self.numList)

obj = RandomizedSet()
print(obj.insert(1))
print(obj.insert(2))
print(obj.insert(3))
print(obj.insert(4))
print(obj.remove(2))
print(obj.getRandom())
print(obj.numList)
print(obj.numMap)


