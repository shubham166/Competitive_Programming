class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        ugly_num = [None] * (1700)
        ugly_num[1] = 1

        i2 = 1
        i3 = 1
        i5 = 1

        for index in range(2, 1700):
            next_ugly_num = min(
                2 * ugly_num[i2],
                3 * ugly_num[i3],
                5 * ugly_num[i5]
            )
            if (next_ugly_num == 2 * ugly_num[i2]):
                i2 = i2 + 1

            if (next_ugly_num == 3 * ugly_num[i3]):
                i3 = i3 + 1

            if (next_ugly_num == 5 * ugly_num[i5]):
                i5 = i5 + 1

            ugly_num[index] = next_ugly_num

            if index > n + 5:
                break

        return ugly_num[n]

s = Solution()
print(s.nthUglyNumber(10))

