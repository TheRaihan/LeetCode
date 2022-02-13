#include <bits/stdc++.h>
using namespace std;


//brute force... TLE
int main()
{
    int x[] = {7, 1, 5, 3, 6, 4};
    int max = 0;
    for (int i = 0; i < 6; i++)
    {
        for (int j = i + 1; j < 6; j++)
        {
            if (x[j] - x[i] > max)
                max = x[j] - x[i];
        }
    }
    cout << max << endl;
    return 0;
}

//

int maxProfit(vector<int>& prices) {
        int mn=INT_MAX;
        int sum=INT_MIN;
        int n=prices.size();
        for(int i=0;i<n;i++){
            mn=min(mn,prices[i]);
            sum=max(sum,prices[i]-mn);
        }
        return sum;
    }
