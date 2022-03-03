class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xffffffff
        while b:
		    sum = (a^b) & mask
			carry = ((a&b)<<1) & mask
            a = sum
			b = carry

		if (a>>31) & 1: # If a is negative in 32 bits sense
			return ~(a^mask) #What the first line means is that if what would be the sign bit in a signed 32 bit integer is set then the number is negative. Shift the sign bit over 31 spots then AND it with a 1 to see if its set.
# What the second line does it returns the two's complement of that number. He gives a solid explanation of how ~(a^mask) is derived to be the two's complement. Normally we'd just flip all the bits and add 1 but we can't do that here.
		return a


