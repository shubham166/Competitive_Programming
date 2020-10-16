class Solution(object):
    def count_inversions(self, numbers):
        if numbers is None:
            return 0

        size = len(numbers)
        if size <= 1:
            return 0
        start = 0
        end = size - 1
        return self.count_inversions_recur(numbers, start, end)

    def count_inversions_recur(self, numbers, start, end):
        if start == end:
            return 0
        mid = (start + end) // 2
        left_inversions = self.count_inversions_recur(numbers, start, mid)
        right_inversions = self.count_inversions_recur(numbers, mid + 1, end)

        cross_inversions = self.count_cross_inversions(numbers, start, mid, end)

        return left_inversions + right_inversions + cross_inversions

    def count_cross_inversions(self, numbers, start, mid, end):
        lsize = mid - start + 1
        rsize = end - mid

        larr = [None] * lsize
        rarr = [None] * rsize

        for index in range(0, lsize):
            larr[index] = numbers[index + start]

        for index in range(0, rsize):
            rarr[index] = numbers[index + mid + 1]

        inversions = 0
        i, j, k = 0, 0, start

        while i < lsize and j < rsize:
            if rarr[j] < larr[i]:
                inversions += lsize - i
                numbers[k] = rarr[j]
                j += 1
            else:
                numbers[k] = larr[i]
                i += 1
            k += 1

        while i < lsize:
            numbers[k] = larr[i]
            i += 1
            k += 1

        while j < rsize:
            numbers[k] = rarr[j]
            j += 1
            k += 1

        return inversions

s = Solution()
# a = s.count_inversions([7, 1, 3, 4, 2, 1, 8, 5])

a = s.count_inversions([6, 5, 4, 3, 2, 1])
print(a)

