class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if prices is None:
            return 0

        size = len(prices)
        if size <= 1:
            return 0

        profit = [0] * size

        max_price = prices[size - 1]
        for index in range(size - 2, -1, -1):
            if prices[index] > max_price:
                max_price = prices[index]

            profit[index] = max(profit[index + 1], max_price - prices[index])
            print(f"Price here = {prices[index]}, profit = {profit[index]}, max_price = {max_price}")

        print(profit)
        min_price = prices[0]
        for index in range(0, size):
            if prices[index] < min_price:
                min_price = prices[index]

            profit[index] = max(profit[index - 1], profit[index] + prices[index] - min_price)
        print(profit)

        return profit[size - 1]





s = Solution()
print(s.maxProfit([8,3,6,2,8,8,8,4,2,0,7,2,9,4,9]))

# print(stockBuySell([1, 2, 4, 2, 5, 7, 2, 4, 9, 0], 10))
