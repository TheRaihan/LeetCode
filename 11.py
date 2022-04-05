class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r,mx = 0, len(height) - 1, 0
        
        while l<=r:
            dis = r-l
            water = dis * min(height[l],height[r])
            mx = max(water,mx)
            
            if (height[l] < height[r]): l+=1 
            else: r-=1
        
        return mx