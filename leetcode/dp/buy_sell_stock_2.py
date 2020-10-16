'''
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
122. Best Time to Buy and Sell Stock II
Greedy Approach

Simplest approach
class Solution {
    public int maxProfit(int[] prices) {
        int maxprofit = 0;
        for (int i = 1; i < prices.length; i++) {
            if (prices[i] > prices[i - 1])
                maxprofit += prices[i] - prices[i - 1];
        }
        return maxprofit;
    }
}
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

        min_val = prices[0]
        max_val = prices[0]
        total_profit = 0

        for index in range(1, size):
            if prices[index] > max_val:
                max_val = prices[index]

            else:
                total_profit = total_profit + (max_val - min_val)
                min_val = prices[index]
                max_val = prices[index]

        total_profit = total_profit + (max_val - min_val)
        return total_profit

s = Solution()
print(s.maxProfit([1,2,3,4,5]))




