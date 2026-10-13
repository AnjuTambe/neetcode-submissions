class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # optimized solution : we keep track of the min price we have seen 
        #so far and find out the profit on that

        min_price = float('inf')
        max_profit = 0

        for price in prices : 
            if price < min_price :

                min_price = price

            profit = price -  min_price

            if profit > max_profit :
                
                max_profit = profit

        return max_profit   



        # n = len(prices)
        # maxprofit = 0

        # for i in range(n): 

        #     for j in range (i+1 , n) :

        #         profit = prices[j] - prices[i] 

        #         maxprofit = max(maxprofit , profit)

        # return   maxprofit      

        