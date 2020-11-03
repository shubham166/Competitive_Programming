import sys

class Solution(object):
    def get_max_product_increasing_subseq_triplet(self, numbers):
        if numbers == None:
            return None

        size = len(numbers)
        if size < 3:
            return None

        lnr = Solution.largest_number_right(numbers)
        lnl = Solution.largest_number_left(numbers)

        max_so_far = -sys.maxsize
        for i in range(1, size - 1):
            product = numbers[i] * lnr[i] * lnl[i]
            max_so_far = max(product, max_so_far)

        return max_so_far

    @staticmethod
    def largest_number_right(numbers):
        size = len(numbers)
        lnr = [-1 for _ in range(size)]
        lnr[size - 1] = -sys.maxsize
        for index in range(size - 2, -1, -1):
            lnr[index] = max(numbers[index + 1], lnr[index + 1])

        return lnr

    @staticmethod
    def largest_number_left(numbers):
        size = len(numbers)
        lnl = [-1 for _ in range(size)]
        lnl[0] = -sys.maxsize

        for index in range(1, size):
            lnl[index] = max(lnl[index - 1], numbers[index - 1])

        return lnl


s = Solution()

arr = [10, 11, 9, 5, 6, 1, 20]
print(Solution.largest_number_right(arr))
print(Solution.largest_number_left(arr))

print(s.get_max_product_increasing_subseq_triplet(arr))

