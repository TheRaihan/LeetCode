class Solution {
public:
    int maxArea(vector<int>& height) {
        int water=0,mx = 0, dis=0;
        
        for(int left = 0, right = height.Length-1 ; left<=right; )
        {
            dis = right - left;
            water = dis * Math.Min(height[left],height[right]);
            if(water > mx)
                mx = water;
            
            if (height[left] < height[right]) 
                left++;
            else 
                right--;
            
        }
        return mx;
    }
};