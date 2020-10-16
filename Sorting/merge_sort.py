class Solution(object):
    def merge_sort(self, numbers):
        if numbers is None:
            return None

        size = len(numbers)
        if size <= 0:
            return numbers

        start = 0
        end = size - 1

        sorted_numbers = self.merge_sort_recur(numbers, start, end)
        return sorted_numbers

    def merge(self, numbers, start, mid, end):
        lsize = mid - start + 1
        rsize = end - mid

        larr = [None] * lsize
        rarr = [None] * rsize

        for index in range(0, lsize):
            larr[index] = numbers[index + start]

        for index in range(0, rsize):
            rarr[index] = numbers[index + mid + 1]

        i, j, k = 0, 0, start

        while i < lsize and j < rsize:
            if larr[i] <= rarr[j]:
                numbers[k] = larr[i]
                i += 1
            else:
                numbers[k] = rarr[j]
                j += 1
            k += 1

        while i < lsize:
            numbers[k] = larr[i]
            i += 1
            k += 1

        while j < rsize:
            numbers[k] = rarr[j]
            j += 1
            k += 1

        return numbers

    def merge_sort_recur(self, numbers, start, end):
        if start == end:
            return numbers

        mid = (start + end) // 2
        numbers = self.merge_sort_recur(numbers, start, mid)
        numbers = self.merge_sort_recur(numbers, mid + 1, end)

        merged_arr = self.merge(numbers, start, mid, end)
        return merged_arr


s = Solution()
a = s.merge_sort([7, 1, 3, 4, 2, 1, 8, 5])
print(a)

