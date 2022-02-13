mn = prices[0]
sm = 0
for stock in prices:
    mn = min(mn, stock)
    sm = max(sm, stock-mn)
print(sm)
