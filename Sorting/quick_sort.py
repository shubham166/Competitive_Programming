class Solution(object):
    def quick_sort(self, numbers):
        if numbers is None:
            return None

        size = len(numbers)
        if size <= 1:
            return numbers
        start = 0
        end = size - 1
        return self.quick_sort_recur(numbers, start, end)

    def quick_sort_recur(self, numbers, start, end):
        # print(f"Start = {start}, end = {end}")
        if start >= end:
            return numbers

        pivot = start
        i = start
        j = start + 1

        while j <= end:
            if numbers[j] < numbers[pivot]:
                numbers[i + 1], numbers[j] = numbers[j], numbers[i + 1]
                i += 1
                j += 1
            else:
                j += 1

        numbers[pivot], numbers[i] = numbers[i], numbers[pivot]
        numbers = self.quick_sort_recur(numbers, start, i - 1)
        numbers = self.quick_sort_recur(numbers, i + 1, end)
        return numbers

s = Solution()
ans = s.quick_sort([3, 4, 8, 1, 2, 7, 6, 5, 8, 9, 3, 32, 2, 3, 3, 2323, 23, 21, 11, 1,2, 23, 23])
print(ans)
l = [3, 4, 8, 1, 2, 7, 6, 5, 8, 9, 3, 32, 2, 3, 3, 2323, 23, 21, 11, 1,2, 23, 23]
ans2 = l.sort()
print(l)