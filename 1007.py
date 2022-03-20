class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        
        for target in [tops[0],bottoms[0]]:
            missT,missB=0,0
            for i in range(len(tops)):
                if tops[i] != target and bottoms[i] != target:
                    break
                
                if tops[i] != target: missT+=1
                if bottoms[i] != target: missB+=1
                
                if i==len(tops)-1:
                    return min(missT,missB)
                
        return -1 