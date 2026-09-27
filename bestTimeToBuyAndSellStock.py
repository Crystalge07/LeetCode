class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0 # starts assuming the max profit is 0
        lowestPrice = prices[0] # the lowest price we currently know of is the first element of the list

        for price in prices: # iterates through the actual prices 
            maxProfit = max(maxProfit, price-lowestPrice) # chooses the max profit between the current max profit we know, or the current price - the lowest price we know of
            lowestPrice = min(lowestPrice, price) # chooses the lowest price between all the prices we've seen before, or the ucrrent price

        return maxProfit

"""
this way is more effecient than simply brute forcing through the list comparing every element
we start by assuming the profit is 0, then that the lowest price we know of is the price of day 1
we then iterate through the list of prices, changing the max profit to the higher between the current max profit we have, or the profit we would have by selling today against our lowest price
we change the lowest price by simply comparing the price of day vs lowest ones in the past
"""        













"""
        # focus on assuming current index is the selling point and we compare to buying point, bc if we use selling point we've alr traversed the array but with assuming the current index is the buying point, it's having to constantly go forward 
        
        maxProfit = 0 #tracking the best profit so far, which is the selling price (today) - the lowest buy price we have seen thus far (the left of the array)
        lowestPrice = prices[0] #tracking which day to buy

        for sellingDay in prices:
            maxProfit = max(maxProfit, sellDay-lowestPrice) # saying that the max profit we can have, is the highest between the current max profit, or the current day's price minus the lowest price we've seen
            lowestPrice = min(lowestPrice, sellingDay) # the lowest price we've seen so far is the min between the lowest price we alr have (0) or 
        return maxProfit


      
        smallest = 0

        for i in range(0, len(prices)): 
            if list[i] > smallest:
                smallest = list[i]
                index = i
        
        biggest = smallest
        for i in list[index:]: # wait im kinda confused abt this part, js how to go through the latter portion of the list to see if theres a value that is bigger than the smallest one 
            if list[i] > smallest:
                biggest = list[i]
        
        difference = biggest - smallest

        if biggest = smallest:
            return 0
        else:
            return difference
            
        
        

# find smallest number in the list, and find the biggest number after it then subtract 
# lmao nvm this does not work cus like [2, 8, 1, 3]
"""



