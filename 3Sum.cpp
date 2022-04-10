class Solution
{
public:
    vector<vector<int>> threeSum(vector<int> &nums)
    {

        vector<vector<int>> res;
        sort(nums.begin(), nums.end());

        for (int i = 0; i < nums.size(); i++)
        {
            int l = i + 1, r = nums.size() - 1;
            if (i != 0 && nums[i] == nums[i - 1])
                continue;
            while (l < r)
            {
                int sum = nums[i] + nums[l] + nums[r];
                if (sum > 0)
                    r--;
                else if (sum < 0)
                    l++;
                else
                {
                    vector<int> triplet = {nums[i], nums[l], nums[r]};
                    res.push_back(triplet);
                    l++;
                    while (nums[l] == nums[l - 1] && l < r)
                        l++;
                }
            }
        }
        return res;
    }
};