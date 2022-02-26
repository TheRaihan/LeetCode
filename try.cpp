// CPP program to initialize a vector like
// an array.
#include <bits/stdc++.h>
using namespace std;

int main()
{
    vector<int> vect, ans;
    set<vector<int> > unique_results;
    int mul = 1, zero = 0, flag = 0;

    vect.push_back(-1);
    vect.push_back(2);
    vect.push_back(0);
    vect.push_back(1);
    vect.push_back(-1);
    vect.push_back(4);

    sort(vect.begin(), vect.end());
    set<vector<int>, greater<int> >::iterator itr;
    int sz = vect.size(), k, sum = 0;

    for (int i = 0; i < sz; i++)
    {
        k = sz - 1;
        for (int j = i + 1; j < sz; )
        {
            if (j == k)
                break;
            sum = vect[i] + vect[j] + vect[k];
            if (sum == 0)
            {
                cout << vect[i] << " " << vect[j] << " " << vect[k--] << " " << endl;
            }
            else if (sum > 0)
            {
                k--;
            }
            else
                j++;
        }
    }

    // vector<vector<int> > results;

    // std::copy(
    //     unique_results.begin(), unique_results.end(),
    //     std::back_inserter(results));

    // for (std::vector<vector<int> >::iterator it = results.begin(); it != results.end(); ++it)
    // {
    //     for (vector<unsigned char>::iterator it1 = (*it).begin(); it1 != (*it).end(); ++it1)
    //     {
    //         cout << *it1 << endl;
    //     }
    // }

    // for (const auto &v : results)
    // {
    //     for (auto i : v)
    //     {
    //         cout << i << endl;
    //     }
    // }
    return 0;
}
