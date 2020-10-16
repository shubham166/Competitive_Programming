'''
https://leetcode.com/problems/climbing-stairs/

70. Climbing Stairs

'''


class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0:
            return 0
        if n == 1:
            return 1
        dp = [0 for i in range(n + 1)]
        dp[1] = 1
        dp[2] = 2

        for index in range(3, n + 1):
            dp[index] = dp[index - 1] + dp[index - 2]
            # print(f"at {index}, {dp[index]}")

        return dp[n]

s = Solution()
print(s.climbStairs(10))