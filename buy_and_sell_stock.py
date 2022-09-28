#121. Best Time to Buy and Sell Stock
test_list = [7, 1, 4, 5, 3, 6, 2]

def maxProfit(prices) -> int:
        buy = 0
        sell = 1
        profit = 0
        max_profit = 0
        
        while sell < len(prices):
            if prices[buy] < prices[sell]:
                profit = prices[sell] - prices[buy]
            else:
                buy = sell
                
            if profit > max_profit:
                max_profit = profit
                
            sell += 1
            
        return max_profit

maxProfit(test_list)