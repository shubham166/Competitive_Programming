class Solution(object):
    def __init(self):
        self.lookup = [[None for wt in range(102)] for elm in range(12)]

    def get_max_value(self, max_weight, weights, values):
        num_elements = len(values)

        return self.get_max_recur(num_elements=num_elements, max_weight=max_weight, weights=weights, values=values)



    def get_max_recur(self, num_elements, max_weight, weights, values):

        if max_weight <= 0 or num_elements <= 0:
            self.lookup[num_elements][max_weight] = 0


        if self.lookup is not None:
            return self.lookup[num_elements][max_weight]

        case1 = self.get_max_cur(num_elements - 1, max_weight - weights[num_elements - 1]) + values[num_elements - 1]
        case2 = self.get_max_cur(num_elements - 1, max_weight)
        self.lookup[num_elements][max_weight] = max(case1, case2)
        return self.lookup