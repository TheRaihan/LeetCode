#include <iostream>
#include <string>

class Solution
{
public:
    string removeDuplicateLetters(string s)
    {

        vector<bool> visited(26, false);
        vector<int> cnt(26, 0);
        string res = "";

        for (auto c : s)
            cnt[c - 'a']++;

        for (int i = 0; i < s.size(); i++)
        {
            cnt[s[i] - 'a']--;
            if (visited[s[i] - 'a'] == true)
                continue;
            while (!res.empty() && res.back() > s[i] && cnt[res.back() - 'a'] > 0)
            {
                visited[res.back() - 'a'] = false;
                res.pop_back();
            }
            visited[s[i] - 'a'] = true;
            res += s[i];
        }

        return res;
    }
};