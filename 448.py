
# O(1) space Solution

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res = []
        
        for x in nums:
            nums[abs(x) - 1] = abs(nums[abs(x) - 1]) * (-1)
        
        for i in range(len(nums)):
            if(nums[i] > 0):
                res.append(i+1)
                
        return res

# for understanding check this
# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/discuss/92958/c%2B%2B-solution-O(1)-space