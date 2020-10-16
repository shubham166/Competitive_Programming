##  https://leetcode.com/problems/ugly-number-iii/
class Solution(object):
    def nthUglyNumber(self, n, a, b, c):
        """
        :type n: int
        :rtype: int
        """
        # ugly_num = [None] * (n + 5)

        # ugly_number = [1]

        ia = 1
        ib = 1
        ic = 1

        for index in range(n):
            next_ugly_num = min(
                a * ia,
                b * ib,
                c * ic
            )
            print(f"Next ugly num = {next_ugly_num}")
            if next_ugly_num == a * ia:
                ia = ia + 1

            if (next_ugly_num == b * ib):
                ib = ib + 1

            if (next_ugly_num == c * ic):
                ic = ic + 1

            # ugly_number.append(next_ugly_num)
        # print(ugly_num[:10])
        return next_ugly_num

s = Solution()
print(s.nthUglyNumber(3, 2, 3, 5))

