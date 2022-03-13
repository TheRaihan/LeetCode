#include <bits/stdc++.h>
using namespace std;

int main()
{
    vector<int> v{5, 4, 3, 2, 4, 5, 12, 1, 24, 5, 6};
    map<int, int> ans;
    // 1 2 3 4 4 5 5 5 6 12 24

    for (int i = 0; i < v.size(); i++)
        ans[v[i]]++;

    for (auto x : ans)
        if (x.second == 1)
            cout << x.first << endl;

    cout << isValid("()[]{}") << endl;
    return 0;
}
