def maxProfit(prices: list[int]) -> int:
    profit = 0
    n = len(prices)
    ##BRUTE FORCE APPROACH
    # for i in range(n):
    #     for j in range(i+1, n):
    #         profit = max(profit, prices[j] - prices[i])
    

    ## MY APPROACH
    # buy = float('inf')
    # sell = float('-inf')
    # for i in range(n):
    #     if prices[i] < buy:
    #         buy = prices[i]
    #         sell = float('-inf')
    #     if prices[i] > sell:
    #         sell = prices[i] 

    #     profit = max(profit, sell - buy)

    ## CORRECT APPROACH
    buy = prices[0]

    for i in range(1, n):
        if prices[i] < buy:
            buy = prices[i]

        profit = max(profit, prices[i] - buy)

    return profit

list = [8, 3, 5, 7, 2, 8, 10]
print(f'maximum profit will be {maxProfit(list)}')