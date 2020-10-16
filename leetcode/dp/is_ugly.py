import math
class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num < 1:
            return False
        if num == 1:
            return True

        pm_list = self.get_prime_factors(num)
        return all(i == 2 or i == 3 or i == 5 for i in pm_list)


    def get_prime_factors(self, num):
        pm_list = []
        flag = False
        while num % 2 == 0:
            flag = True
            num = num / 2
        if flag:
            pm_list.append(2)

        for prime_factor in range(3, int(math.sqrt(num)) + 1, 2):
            flag = False
            while num % prime_factor == 0:
                flag = True
                num = num / prime_factor
                print(f"num = {num}")
            if flag:
                pm_list.append(prime_factor)

        if num > 2:
            pm_list.append(num)

        return pm_list



s = Solution()
print(s.get_prime_factors(8))

