class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        map = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }
        
        for x in s:
            if x in map:
                if stack and stack[-1] == map[x]:
                    stack.pop()
                else: 
                    return False
            else:
                stack.append(x)
        
        return True if not stack else False