class Solution {
public:
    int maxArea(vector<int>& height) {
        int water=0,mx = 0, dis=0;
        
        for(int left = 0, right = height.size()-1 ; left<=right; )
        {
            dis = right - left;
            // cout<< dis << " " << height[left] << " " << height[right]<< endl;
            water = dis * min(height[left],height[right]);
            if(water > mx)
                mx = water;
            
            (height[left] < height[right]) ? left++ : right --;
            
        }
        return mx;
    }
};