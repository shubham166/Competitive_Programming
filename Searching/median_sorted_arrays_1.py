'''
https://www.geeksforgeeks.org/median-of-two-sorted-arrays/
O(logN) solution)
'''
class Solution(object):
    def get_median(self, arr1, arr2):       # size of both the array should be equal and array should be sorted
        if arr1 is None or arr2 is None:
            return None

        size1 = len(arr1)
        size2 = len(arr2)

        assert(size1 == size2)


        return self.get_median_recur(arr1, arr2, 0, 0, size1 - 1, size1 - 1)


    def get_median_recur(self, arr1, arr2, st1, st2, end1, end2):
        if end1 - st1 <= 2:
            med1 = max(arr1[0], arr2[0])
            med2 = min(arr1[1], arr2[0])

            return (med1 + med2) / 2

        mid1 =

# function to find median of array
def median(arr, n):
    if n % 2 == 0:
        return (arr[int(n / 2)] +
                arr[int(n / 2) - 1]) / 2
    else:
        return arr[int(n / 2)]