#include <bits/stdc++.h>
using namespace std;

int main()
{
    int bills[] = {5, 5, 5, 5, 20, 20, 5, 5, 5, 5};
    int five = 0, ten = 0;
    for (int i = 0; i < sizeof(bills) / sizeof(bills[0]); i++)
    {
        if (bills[i] == 5)
            five++;
        else if (bills[i] == 10)
        {
            five--;
            ten++;
        }
        else if (bills[i] == 20)
        {
            five--;
            ten--;
        }
        if (ten < 0 && five > 2)
        {
            ten++;
            five -= 2;
        }
        if (five < 0 || ten < 0)
            return false;
    }
    return true;
}
