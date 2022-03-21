class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        res = []
        sum = 0
        for bit in nums:
            sum = ( sum*2 + bit ) % 5
            res.append(sum == 0)
        
        return res