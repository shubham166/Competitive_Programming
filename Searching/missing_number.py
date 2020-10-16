"""
https://www.geeksforgeeks.org/find-the-missing-number/
"""

class Solution(object):
    def find_missing_number(self, numbers):
        if numbers is None:
            return None

        size = len(numbers)
        if size <= 1:
            return -1

        x1 = numbers[0]

        x2 = 1

        for index in range(1, size):
            x1 = x1 ^ numbers[index]

        for index in range(2, size + 2):
            x2 = x2 ^ index

        return x1 ^ x2

s = Solution()
a = s.find_missing_number([1, 3, 4, 5])
print(a)