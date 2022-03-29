class Solution {
public:
    int climbStairs(int n) {
        int one = 1,two = 1;
        int tmp;
        n--;
        while(n--)
        {
            tmp = one;
            one = one + two;
            two = tmp;
        }
        return one;
    }
};