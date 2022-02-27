class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sm = 0;
        n = len(nums)
        total = n*(n+1)/2
        for x in nums:
            sm+=x
        return int(total-sm)