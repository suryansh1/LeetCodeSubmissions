class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        profit = 0
        
        # Brute force approach
        
        # For each index i
        # Calculate profit from n-i future days and store max 
        
        lowest_buy_price = sys.maxsize
        
        
        for i, buy_price in enumerate(prices) : 
            
            if buy_price < lowest_buy_price:  lowest_buy_price = buy_price
            
            if prices[i] - lowest_buy_price > profit : 
                
                profit = prices[i] - lowest_buy_price
                    
                    
        return profit