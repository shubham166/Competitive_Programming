'''
https://www.geeksforgeeks.org/sort-elements-by-frequency/
'''
import functools

class Solution(object):
    def sort_by_frq(self, numbers):
        if numbers is None:
            return None
        size = len(numbers)
        if size <= 1:
            return numbers

        freq_arr = []


        sorted_numbers = sorted(numbers)
        prev_num = sorted_numbers[0]
        st_index = 0
        freq = 1

        def compare(tup1, tup2):
            if tup1[1] > tup2[1]:
                return -1
            elif tup1[1] < tup2[1]:
                return 1
            else:
                if tup1[2] < tup2[2]:
                    return -1
                else:
                    return 1


        for index in range(1, size):
            if sorted_numbers[index] != prev_num:
                freq_arr.append((prev_num, freq, st_index))
                st_index = index
                prev_num = sorted_numbers[index]
                freq = 1
            else:
                freq += 1

        freq_arr.sort(key=functools.cmp_to_key(compare))

        final_list = []
        for index in range(len(freq_arr)):
            for freq in range(freq_arr[index][1]):
                final_list.append(freq_arr[index][0])

        return final_list


s = Solution()
ans = s.sort_by_frq([2, 5, 2, 6, -1, 9999999, 5, 8, 8, 8])
print(ans)