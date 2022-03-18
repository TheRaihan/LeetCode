class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        cnt= Counter(s)
        visited = set()
        stack = []
        
        for c in s:
            cnt[c]-=1
            if c not in visited:
                while stack and stack[-1] > c and cnt[stack[-1]] > 0:
                    visited.remove(stack.pop())
                visited.add(c)
                stack.append(c)
                
        return "".join(stack)
        