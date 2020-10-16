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

        if numbers[mid] == num:
            return mid

        if numbers[start] <= numbers[mid]:      # First half is sorted
            if num < numbers[mid] and num >= numbers[start]:
                index = self.binary_search_recur(numbers, start, mid - 1, num)
            else:
                index = self.binary_search_recur(numbers, mid + 1, end, num)

        elif numbers[end] >= numbers[mid]:           # second half is sorted

           if num > numbers[mid] and num <= numbers[end]:
               index = self.binary_search_recur(numbers, mid + 1, end, num)
           else:
               index = self.binary_search_recur(numbers, start, mid - 1, num)

        return index


s = Solution()
a = s.binary_search([4, 5, 6, 7, 8, 1, 2, 3], 4)
print(a)