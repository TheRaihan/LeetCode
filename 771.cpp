#include <bits/stdc++.h>
using namespace std;

int main()
{
    int a = 5, b = 7;
    long long c = 0;

    while (b != 0)
    {
        c = a & b;
        a = a ^ b;
        b = (unsigned int)c << 1;
    }
    cout << a << endl;
}