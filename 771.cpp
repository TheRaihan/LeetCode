#include <bits/stdc++.h>
using namespace std;

int main()
{
    int x[] = {-2, 1, -3, 4, -1, 2, 1, -5, 4}, sz = 9;
    int sum = 0;
    int mx = x[0];
    for (int i = 0; i < sz; i++)
    {
        if (mx + x[i] > mx)
        {
            mx = mx + x[i];
        }
        else if (x[i] > mx)
        {
            mx = x[i];
        }
    }
    return 0;
}