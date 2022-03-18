#include <iostream>
#include <string>

class Solution {
public:
    string removeDuplicateLetters(string s) {
        bool visited[26] = {0};
        int cnt[26] = {0};
        string res="";
        
        for(int i=0 ; i<s.size();i++)
            cnt[ s[i] - 'a' ]++;
        
        for(int i=0 ; i<s.size();i++)
        {
            
            cnt[ s[i] - 'a' ]--;
            if(visited[ s[i] - 'a' ]) continue;
            while(!res.empty() && res.back() > s[i] && cnt[ res.back() - 'a' ] > 0 )
            {
                visited[ s[i] - 'a'] = false;
                res.pop_back();
            }
            visited[ s[i] - 'a'] = true;
            res+=s[i];
         }
        
        return res;
    }
};