class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        #dynamic solution
        #keep track of min to record seen

        minPrice = float('inf')
        maxProf = 0

        for p in prices:
            profit = p - minPrice
            maxProf = max(profit, maxProf)
            minPrice =  min(p, minPrice)

        return maxProf


        #Pointer Solution
        #pl, pr = 0,1
        
        #maxProf = 0
        #while (pr < len(prices)):
        #    if (prices[pl] < prices[pr]):
        #        profit = prices[pr] - prices[pl]
        #        maxProf = max(profit, maxProf)
        #    else: 
        #        pl = pr
        #    pr+=1
        #return maxProf
