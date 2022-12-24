from aoc2022.day import Day
from functools import cmp_to_key

class Day13 (Day):
    def __init__(self):
        super().__init__(__name__)
        self._isdone = True
        self._lines = self.read_file_lines()

    @staticmethod
    def in_order(l_a, l_b, is_inner=False):
        for i in range(len(l_a)):
            if i >= len(l_b):
                return False
            el_a = l_a[i]
            el_b = l_b[i]
            if type(el_a) != type(el_b):
                el_a = el_a if type(el_a) == list else [el_a]
                el_b = el_b if type(el_b) == list else [el_b]
            if type(el_a) == int:
                if el_a > el_b:
                    return False
                elif el_a < el_b:
                    return True
            else:
                inner_order = Day13.in_order(el_a, el_b, is_inner=True)
                if inner_order is None:
                    continue
                return inner_order
        res = None if is_inner else True
        if len(l_b) > len(l_a):
            res = True
        return res

    @staticmethod
    def cmp(l_a, l_b):
        if Day13.in_order(l_a, l_b):
            # left is "smaller"
            return -1
        return 1

    def solve_1(self):
        #lines = open("13.txt", "r").readlines()
        sum = 0
        idx_pair = 1
        for i in range(0, len(self._lines), 3):
            l_a = eval(self._lines[i])
            l_b = eval(self._lines[i+1])
            if Day13.in_order(l_a, l_b):
                sum += idx_pair
            idx_pair += 1
        return sum


    def solve_2(self):
        packets = [eval(s) for s in self._lines if s.strip() != ""]
        packets.append([[2]])
        packets.append([[6]])
        packets.sort(key=cmp_to_key(Day13.cmp))
        idx_2 = 0
        idx_6 = 0
        for i in range(len(packets)):
            if packets[i] == [[2]]:
                idx_2 = i+1
            if packets[i] == [[6]]:
                idx_6 = i+1
        return idx_2*idx_6
