'''
https://www.geeksforgeeks.org/two-elements-whose-sum-is-closest-to-zero/
'''
import sys

class Solution(object):
    def get_min_sum(self, numbers):
        if numbers is None:
            return None
        size = len(numbers)
        if size <= 1:
            return None

        numbers_sorted = sorted(numbers)

        st, end = 0, size - 1

        sum = sys.maxsize
        while st < end:
            temp = numbers_sorted[st] + numbers_sorted[end]
            if abs(temp) < abs(sum):
                min_l = numbers_sorted[st]
                min_r = numbers_sorted[end]
                sum = temp
            if temp < 0:
                st += 1
            else:
                end -= 1

        return sum, min_l, min_r

s = Solution()

ans = s.get_min_sum([1, 60, -10, 70, -80, 85])
print(ans)

