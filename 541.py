class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        s=list(s)
        for i in range(0,len(s),2*k):
            s[i:i+k]=(s[i:i+k])[::-1]
        return ''.join(s)



class Solution {
public:
    string reverseStr(string s, int k) {
        int sz = s.size();
        for(int i = 0 ;i < sz-1 ; i+=(2*k))
        {
            int start = i, end = min(i+k-1,sz-1);
            while( start <= end )
                swap(s[start++],s[end--]);
        }
        return s;
    }
};