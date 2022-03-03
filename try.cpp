// CPP program to initialize a vector like
// an array.
#include <bits/stdc++.h>
using namespace std;

int main()
{
    vector<int> nums{ 4,1,2,1,2 };
    int ans = 0;
    for (int x : nums)
        ans = ans ^ x;

    cout << ans << endl;
    return 0;
}
