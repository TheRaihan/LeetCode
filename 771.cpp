#include <bits/stdc++.h>
using namespace std;

int main()
{

    int missingNumber(vector<int> & nums)
    {
        int result = nums.size();
        int i = 0;

        for (int num : nums)
        {
            result = result ^ num;
            result = result ^ i;
            i++;
        }

        return result;
    }
}