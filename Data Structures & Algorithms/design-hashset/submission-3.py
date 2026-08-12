class MyHashSet:

    def __init__(self):
        self.arr = {}
    def add(self, key: int) -> None:
        self.arr[key] = True
    def remove(self, key: int) -> None:
        self.arr.pop(key,None)
    def contains(self, key: int) -> bool:
        return self.arr.get(key,False)

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)