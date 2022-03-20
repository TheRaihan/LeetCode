class FreqStack:

    def __init__(self):
        self.mx = 0
        self.freq = {}
        self.stacks = {}

    def push(self, val: int) -> None:
        cntVal = 1 + self.freq.get(val,0)
        self.freq[val] = cntVal
        
        if cntVal > self.mx:
            self.mx = cntVal
            self.stacks[cntVal] = []
        self.stacks[cntVal].append(val)
        

    def pop(self) -> int:
        val = self.stacks[self.mx].pop()
        self.freq[val] -= 1
        if not self.stacks[self.mx]:
            self.mx -= 1
        return val


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()



