class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lptr, rptr = 0, len(prices) - 1
        maxprofit = 0
        minprice = float(inf)
        for it in range(len(prices)):
            if prices[it] < minprice:
                minprice = prices[it]
            elif (prices[it] - minprice > maxprofit):
                maxprofit = prices[it] - minprice
        return maxprofit

        # wrong        
        # cnter = 0
        # while (cnter <= len(prices) ):
        #     cnter += 1
        #     print('prices[rptr]: ', prices[rptr], ', prices[lptr]: ', prices[lptr])
        #     if lptr + 1 <= len(prices)-1 and prices[lptr + 1] < prices[lptr]:
        #         lptr += 1
        #     if rptr > 0 and prices[rptr - 1] > prices[rptr]:
        #         rptr -= 1
        #     maxprofit = max(maxprofit, prices[rptr] - prices[lptr])
        # return maxprofit
        