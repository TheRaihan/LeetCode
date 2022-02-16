// CPP program to initialize a vector like
// an array.
#include <iostream>
#include <vector>
using namespace std;

int main()
{
    vector<int> vect, ans;
    int mul = 1, zero = 0, flag = 0;

    vect.push_back(-1);
    vect.push_back(1);
    vect.push_back(0);
    vect.push_back(-3);
    vect.push_back(0);
    for (int i = 0; i < vect.size(); i++)
    {
        if (vect[i] == 0)
        {
            zero++;
            flag = i;
            continue;
        }
        mul = mul * vect[i];
    }

    for (int i = 0; i < vect.size(); i++)
    {
        if (zero > 0)
        {
            ans.push_back(0);
        }
        else
            ans.push_back(mul / vect[i]);
    }

    if (zero == 1)
        ans[flag] = mul;

    cout << mul << endl;

    for (int i = 0; i < vect.size(); i++)
    {
        cout << ans[i] << " ";
    }

    return 0;
}
