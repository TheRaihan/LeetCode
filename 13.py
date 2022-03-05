roman = {'M': 1000,
         'D': 500 ,
         'C': 100,
         'L': 50,
         'X': 10,
         'V': 5,
         'I': 1
         }
#  IV IX 4 9
#  XL XC 40 90
#  CD CM 400 900
# s = "MCMXCIV" # 1000 -100 + 1000 -10 + 100 -1 + 5
total = 0
sz = len(s)
for i in range(0,sz-1):
    if roman[s[i]] < roman[s[i+1]]:
        total -= roman[s[i]]
    else:
        total += roman[s[i]]

total += roman[s[sz-1]]

print(total)

