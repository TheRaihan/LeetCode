#include <bits/stdc++.h>

using namespace std;

int main()
{
    pid_t pid;
    int i = 0;

    pid = fork();

    if(pid > 0)
    {
        i++;
    }
    else if(pid < 0)
    {
        return 1;
    }

    fork();

    cout << i << endl;

    
    // string x[100]; // assuming max number of attendees will be 100
    // int n, m, c = 0, mx = 0;
    // int cnt[100] = {0}; // all value of cnt array is 0
    // cin >> n >> m;

    // for (int i = 0; i < n; i++)
    //     cin >> x[i];

    // for (int i = 0; i < n - 1; i++)
    // {
    //     for (int j = i + 1; j < n; j++)
    //     {
    //         c = 0;
    //         for (int k = 0; k < m; k++)
    //         {
    //             if (x[i][k] == '1' || x[j][k] == '1')
    //                 c++;
    //         }
    //         if (c > mx)
    //             mx = c;
    //         cnt[c]++;
    //     }
    // }

    // cout << "Maximum topic a team can know : " << mx << endl;

    // cout << "Maximum team can be formed : " << cnt[mx] << endl;

    return 0;
}