class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        c = 0
        
        for ch in s: c = c ^ ord(ch)
        for ch in t: c = c ^ ord(ch)
            
        return chr(c)

    


    int sizeS,sizeT,sum1,sum2;
    
    for(int i=0; i< max(sizeS,sizeT); i++)
    {
        if(i<sizeS)
            sum1+=s[i];

        if(i<sizeT)
            sum2+=t[i];
    }

    return abs(sum1-sum2);
