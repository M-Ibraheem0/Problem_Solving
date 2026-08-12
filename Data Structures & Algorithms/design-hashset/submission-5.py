class MyHashSet:

    def __init__(self):
        self.size = 1000
        self.bucket = [[] for _ in range(self.size)]
    def _hash(self,key:int):
        return key % self.size
    def add(self, key: int) -> None:
        h = self._hash(key)
        if key not in self.bucket[h]:
            self.bucket[h].append(key)
    def remove(self, key: int) -> None:
        h = self._hash(key)
        if key in self.bucket[h]:
            self.bucket[h].remove(key)
    def contains(self, key: int) -> bool:
        h = self._hash(key)
        return key in self.bucket[h]

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)