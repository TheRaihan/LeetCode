                    res.append(x);
#include <string>

class Solution {
public:
    string reverseWords(string s) {
        stack<char> st;
        string res;
        string x;
        for(int i=0;i<s.size();i++)
        {
            if(s[i] != ' ')
                st.push(s[i]);
    
            else{
                
                while(!st.empty())
                {
                    x = st.top();
                    st.pop();
                    res.append(x);
                }
                res.append(" ");
            }
        }
        while(!st.empty())
        {
            x = st.top();
            st.pop();
            res.append(x);
        }
        return res;
    }
};