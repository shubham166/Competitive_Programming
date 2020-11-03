'''
https://www.geeksforgeeks.org/minimum-length-unsorted-subarray-sorting-which-makes-the-complete-array-sorted/
'''

class Solution(object):
    def get_min_length_subarray(self, numbers):
        if numbers is None:
            return None

        size = len(numbers)
        if size <= 1:
            return numbers

        st = -1
        end =  -1

        for index in range(size - 1):
            if numbers[index] > numbers[index + 1]:
                st = index
                break

        for index in range(1, size):
            if numbers[index] < numbers[index - 1]:
                end = index
                break

        for