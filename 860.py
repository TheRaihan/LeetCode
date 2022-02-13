five = ten = 0
for value in bills:
    if value == 5:
        five +=1
    elif value == 10:
        five -=1
        ten+=1
    if ten<0 and five >=2:
        ten+=1
        five-=2
    if five < 0 or ten < 0
        return false
    return true