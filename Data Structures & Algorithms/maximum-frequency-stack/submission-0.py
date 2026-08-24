from collections import defaultdict
class FreqStack:
    def __init__(self):
        self.freq_stack = defaultdict(list)
        self.freq_counter = defaultdict(int)
        self.current_max = 0
    def push(self, val: int) -> None:
        self.freq_counter[val] += 1
        self.freq_stack[self.freq_counter[val]].append(val)
        self.current_max = max(self.current_max,self.freq_counter[val])
    def pop(self) -> int:
        val = self.freq_stack[self.current_max].pop()
        self.freq_counter[val] -= 1
        if len(self.freq_stack[self.current_max]) == 0:
            self.current_max -= 1
        return val


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()