#include <bits/stdc++.h>

using namespace std;

int main()
{
    stack<char> st;
    string x = "Mountains are calling";

    for (int i = 0; i < x.size(); i++)
    {
        if (x[i] != ' ' && i != x.size() - 1)
            st.push(x[i]);

        else
        {
            while (!st.empty())
            {
                cout << st.top();
                st.pop();
            }
            if (i != x.size() - 1)
                cout << " ";
        }
    }
    cout << endl;
    return 0;
}