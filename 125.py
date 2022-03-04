import re

s = "A man, a plan, a canal: Panama"


str = re.sub(r'[\W_]+', '', s.lower())

print(str)
print(str[::-1])

return str==str[::-1]