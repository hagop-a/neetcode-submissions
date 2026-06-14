class Solution {
    public int maxProfit(int[] prices) {
        int pl = 0; // should always point to min val
        int pr = 1; // increments through left to right

        int maxProf = 0; 
        int profit = 0; 
        
        //if prices[pl] < min 
        //    min = prices[pl];
        while (pr < prices.length) {
            if (prices[pl] < prices[pr]) {
                profit = prices[pr] - prices[pl];
                maxProf = Math.max(profit, maxProf);
            }
            else {
                pl = pr;
            }
            pr++;
        }
        return maxProf;
    }
}

    /* O(n^2) performance
    public int maxProfit(int[] prices) {

        int max = 0;
        int profit = 0;

        for (int i = 0; i < prices.length-1; i++) {
            for (int j = i; j < prices.length-i; j++) {
                profit = prices[j] - prices[i];
                if (profit > max) 
                    max = profit;
            }
        }
        return max;
    }
    */


/* 
order matters
profit = prev day - next day
*/