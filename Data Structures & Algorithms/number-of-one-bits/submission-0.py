class Solution:
    def hammingWeight(self, n: int) -> int:
        
        
        res = 0
        while n:
            res += n % 2
            n = n >> 1
        return res 

        #subtract it by powers of 2 starting at 2^i-1, where i is the index at which when n is divided by 2^i < 1
    