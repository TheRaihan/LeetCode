nums = [-1,1,0,-3,0]
ans = []
mul = 1
zero = flag = 0

for i,x in enumerate(nums):
    if x == 0:
        zero+=1
        flag = i
        continue
    mul *= x

for i,x in enumerate(nums):
    if zero > 0:
        ans.append(0)
    else:
        ans.append(int(mul/nums[i]))

if zero == 1:
    ans[flag] = mul
for x in ans:
    print(x)

