s = "abcdcbza"

left, right = 0, len(s)-1

while left < right:
    if s[left] != s[right]:
        one, two = s[i:j], s[i+1:j+1]
        return one == one[::-1] or two == two[::-1]
    left, right = left+1, right+1
return True

