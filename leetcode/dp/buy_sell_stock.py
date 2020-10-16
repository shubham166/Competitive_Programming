'''
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/


'''


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if prices is None:
            return 0
        size = len(prices)
        if size <= 0:
            return 0
        max_profit = 0


        max_index, max_val = 0, prices[0]
        min_index, min_val = 0, prices[0]
        for index in range(1, size):
            if prices[index] > max_val:
                max_index = index
                max_val = prices[index]
            elif prices[index] < min_val:
                min_index = index
                min_val = prices[index]

                max_index = index
                max_val = prices[index]

            max_profit = max(
                max_profit,
                max_val - min_val
            )
        return max_profit


s = Solution()
print(s.maxProfit([2, 4, 1]))


