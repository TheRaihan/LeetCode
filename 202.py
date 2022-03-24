class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        # sm = 0
        while n not in seen:
            seen.add(n)
            
            # for x in str(n):
            #     sm += int(x) ** 2
            # n = sm

            n = sum([int(x) **2 for x in str(n)])
        return n == 1