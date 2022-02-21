nums = [-2,1,-3,4,-1,2,1,-5,4]
sm = 0;
mx = float("-inf")

for i in range(len(nums)):
    sm += nums[i]
    if sm > mx:
        mx = sm
    if sm<0:
        sm = 0

print(mx)