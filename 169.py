class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt = 1
        ans = nums[0]
        
        for i in range(1,len(nums)):
            if nums[i] == ans:
                cnt+=1
            elif cnt == 0:
                ans = nums[i]
                cnt=1
            else:
                cnt-=1
                
        return ans