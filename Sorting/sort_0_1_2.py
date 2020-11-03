class Solution(object):
    def sort_0_1_2(self, numbers):
        if numbers is None:
            return None

        size = len(numbers)
        if size <= 1:
            return numbers

        lo = 0
        mid = 0
        hi = size - 1

        while mid <= hi:
            if numbers[mid] == 0:
                numbers = Solution.swap(lo, mid, numbers)
                lo += 1
                mid += 1
            elif numbers[mid] == 1:
                mid += 1
            elif numbers[mid] == 2:
                numbers = Solution.swap(mid, hi, numbers)
                hi -= 1

        return numbers


    @staticmethod
    def swap(i, j, numbers):
        if i >= 0 and j >= 0:
            numbers[i], numbers[j] = numbers[j], numbers[i]

        return numbers



s = Solution()

ans = s.sort_0_1_2([0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1])
print(ans)

