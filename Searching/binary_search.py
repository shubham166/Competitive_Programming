class Solution(object):
    def binary_search(self, numbers, num):
        if numbers is None:
            return None

        size = len(numbers)
        if size <= 0:
            return -1

        start = 0
        end = size - 1
        return self.binary_search_recur(numbers, start, end, num)

    def binary_search_recur(self, numbers, start, end, num):

        if start > end:
            return -1

        mid = (start + end) // 2
        print(f"Start = {start}, end = {end}, mid = {mid}")
        if numbers[mid] == num:
            return mid

        if numbers[mid] > num:
            index = self.binary_search_recur(numbers, start, mid - 1, num)

        else:
            index = self.binary_search_recur(numbers, mid + 1, end, num)
        return index


s = Solution()
a = s.binary_search([2, 3, 4, 6, 7, 9], 1)
print(a)