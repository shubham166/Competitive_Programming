'''
https://www.geeksforgeeks.org/maximum-and-minimum-in-an-array/
'''

class Solution(object):
    def min_max(self, arr):
        size = len(arr)
        if size == 1:
            return arr[0], arr[0]

        if size == 2:
            return arr[0], arr[1]

        min_n = None
        max_n = None
        index = None
        if size % 2 == 0:       # One comparison
            min_n = min(arr[0], arr[1])
            max_n = max(arr[0], arr[1])
            st_index = 2

        else:
            min_n = arr[0]
            max_n = arr[0]
            st_index = 1
        for index in range(st_index, size, 2):
            if arr[index] < arr[index + 1]:
                min_n = min(arr[index], min_n)
                max_n = max(arr[index + 1], max_n)
            else:
                min_n = min(arr[index + 1], min_n)
                max_n = max(arr[index], max_n)

        return min_n, max_n

s = Solution()
ans = s.min_max([1000, 11, 445, 1, 330, 3000] )
print(ans)