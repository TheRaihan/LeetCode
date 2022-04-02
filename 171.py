class Solution {
public:
    int titleToNumber(string columnTitle) {
        int ans=0, x;
        for(char c: columnTitle)
        {
            x = c - 'A' + 1;
            ans = ans * 26 + x;
        }
        return ans;

    }
};