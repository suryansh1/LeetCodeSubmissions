class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        max_profit = 0
        
        min_price = sys.maxsize
        
        for i, price in enumerate(prices) : 
            
            if price < min_price : 
                min_price = price
                
            if price - min_price > max_profit : 
                max_profit = price - min_price
                    
        return max_profit