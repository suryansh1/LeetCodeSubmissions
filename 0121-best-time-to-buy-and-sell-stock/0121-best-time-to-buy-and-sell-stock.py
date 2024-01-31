class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # profit = difference between min_price and future max price


        # Scan through the list

        # A candidate day price can either be

        # 1. Lowest price ever seen

            #   In this case, min_price = cur_price

        # Price which increases profit, cur_price - min_price > profit

        if len(prices) == 0 : return 0

        min_price = prices[0]
        max_profit = 0

        for cur_price in prices:

            if cur_price < min_price : 

                min_price = cur_price

            elif cur_price - min_price > max_profit :

                max_profit = cur_price - min_price


        return max_profit

        #   cur_price, min_price, max_profit
        #   7,7,0
        #   1,1,0
        #   5,1,4
        #   3,1,4
        #   6,1,5
        #   4,1,5


