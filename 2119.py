class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        return True if not num else num%10
        
        
        # return not num or num%10
        
        # if num == 0:
        #     return True
        # else:
        #     return num%10

        # return num == 0 ? true : num % 10;        c++
