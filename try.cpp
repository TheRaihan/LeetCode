#include <bits/stdc++.h>
using namespace std;

bool vowel(char x)
{
    string a = "aeiouAEIOU";
    for (int i = 0; i < a.size(); i++)
    {
        if (a[i] == x)
            return true;
    }
    return false;
}

int main()
{
    string s = "leetcode";
    for (int i = 0, j = s.size() - 1; i < j;)
    {
        cout << s[i] << " " << s[j] << endl;
        if (vowel(s[i]) && vowel(s[j]))
        {
            swap(s[i], s[j]);
            i++;
            j--;
        }
        if (!vowel(s[i]))
            i++;
        if (!vowel(s[j]))
            j--;
        cout << s << endl;
    }
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
