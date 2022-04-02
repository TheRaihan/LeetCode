#include <bits/stdc++.h>
using namespace std;


    char findTheDifference(string s, string t) {
        char r=0;
        for(char c:s) r ^=c;
        for(char c:t) r ^=c;
        return r;
}

//67class Solution {
public:
    string addBinary(string a, string b) {
        
        int i = a.size() - 1;
        int j = b.size() - 1;
        int sum = 0,carry = 0;
        string ans;

        while( i >= 0 || j >= 0)
        {
            sum  = carry;
            if(i >= 0)  sum += a[i--] - '0';
            if(j >= 0)  sum += b[j--] - '0';
            carry = sum > 1 ? 1 : 0;
            ans += to_string(sum%2);
        }

        if(carry)  ans += to_string(carry);
        
        reverse(ans.begin(),ans.end());
        return ans;
        to_integer
    }
};




int main()
{
}

// // CPP program to initialize a vector like
// // an array.
// #include <bits/stdc++.h>
// using namespace std;

// int main()
// {
//     vector<int> list1{1, 2, 3}, list2{4, 5, 6}, list3;
//     int i = 0, j = 0, flag1 = 0, flag2 = 0;
//     while (list3.size() < list1.size() + list2.size())
//     {
//         if (flag1 == 1 && flag2 == 1)
//             break;
//         if (list1[i] <= list2[j] && list3.size() < list1.size() + list2.size())
//         {
//             list3.push_back(list1[i++]);
//             if (i == list1.size())
//             {
//                 i--;
//                 flag1 = 1;
//             }
//         }
//         if (list2[j] <= list1[i] && list3.size() < list1.size() + list2.size())
//         {
//             list3.push_back(list2[j++]);
//             if (j == list2.size())
//             {
//                 j--;
//                 flag2 = 1;
//             }
//         }
//     }
//     cout << i << " " << j << endl;
//     for (int x : list3)
//         cout << x << " ";

//     return 0;
// }
