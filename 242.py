
#1

class Solution {
public:
    bool isAnagram(string s, string t) {
        
        int cnt[26]={0};
        
        if(s.size() != t.size()) return false;
        
        for(int i=0;i<s.size();i++)
        {
            cnt[s[i] - 'a']++;
            cnt[t[i] - 'a']--;
        }
        
        for(int i=0;i<26;i++)
            if(cnt[i])
                return false;

    
        return true;
    }
};

#2
sort(s.begin(), s.end());
sort(t.begin(), t.end());
return s == t; 