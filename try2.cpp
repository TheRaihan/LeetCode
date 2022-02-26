#include <bits/stdc++.h>
using namespace std;

int main()
{
    int n = 01011;
    int ans=0;
    while(n>0)
    {
        ans += n%10;
        cout << n%10 << endl;
        n = n/10;
    }
    return 0;
}