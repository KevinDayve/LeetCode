def maxProfit(prices):
  maxProfit = 0
  cheapest = prices[0]
  
  for i in range(1, len(prices)):
    if prices[i] < cheapest:
      cheapest = prices[i]
      
    current = prices[i] - cheapest
    maxProfit = max(maxProfit, current)
    
  return maxProfit
      
