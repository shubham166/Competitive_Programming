'''
https://leetcode.com/problems/maximum-subarray/
[-2,1,-3,4,-1,2,1,-5,4]

Sol1: a) DP typical, used the memory efficient approach - O(n ^ 2)
Sol2: b) Kadane Algorithm
def maxSubArraySum(a, size):
    max_so_far = -1 * 2 ** 31
    max_ending_here = 0

    for i in range(0, size):
        max_ending_here = max_ending_here + a[i]
        if (max_so_far < max_ending_here):
            max_so_far = max_ending_here

        if max_ending_here < 0:
            max_ending_here = 0
    return max_so_far

'''

class Solution(object):
    def maxSubArray_bak(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # bottom up
        if nums is None or len(nums) <= 0:
            return 0

        l = len(nums)

        # dp = [[0 for col in range(l + 5)] for row in range(l + 5)]
        prev = 0
        cur = 0

        max_value = -1 * 2 ** 31
        for i in range(1, l + 1):
            for j in range(i, l + 1):

                if i == j:
                    # dp[i][j] = nums[j - 1]
                    cur = nums[j - 1]
                    prev = nums[j - 1]
                else:

                    # dp[i][j] = dp[i][j - 1] + nums[j - 1]
                    cur = prev + nums[j - 1]
                    prev = prev + nums[j - 1]
                if cur > max_value:
                    max_value = cur
                # print(f"Value ({i}, {j}) = {dp[i][j]}")
        return max_value

    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_global = nums[0]
        max_local = nums[0]
        size = len(nums)

        for index in range(1, size):
            if max_local < 0:
                max_local = 0

            max_local = max_local + nums[index]

            if max_global < max_local:
                max_global = max_local

        return max_global






s = Solution()
print(s.maxSubArray([-2, -1, 1, 2, -4]))

