class Solution:
    def addDigits(self, num: int) -> int:
        while 1:
            sum = 0
            while num!=0:
                temp = num%10
                num = num//10
                sum += temp
            if sum<10 : return sum
            num = sum