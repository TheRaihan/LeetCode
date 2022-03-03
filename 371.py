class Solution:
    def getSum(self, a: int, b: int) -> int:
        c = 0
        while(b!=0):
            c = a&b
            a = a^b
            b = c << 1
        return a
