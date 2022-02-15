jewels = "aA"
stones = "aAAbbbb"

flag = {}
cnt = 0

for char in stones:
    flag[char] = 0

for char in jewels:
    flag[char] = 1

for char in stones:
    if(flag[char] == 1):
        cnt+=1
return cnt



