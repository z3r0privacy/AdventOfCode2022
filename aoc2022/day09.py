from aoc2022.day import Day

class Day09 (Day):
    def __init__(self):
        super().__init__(__name__)
        self._isdone = True
        self._moves = self.read_file_lines()

    @staticmethod
    def _t_add(t1, t2):
        return t1[0]+t2[0], t1[1]+t2[1]

    @staticmethod
    def _is_close(pH, pT, include_diag=False):
        if abs(pH[0]-pT[0]) + abs(pH[1] - pT[1]) <= 1:
            return True
        if include_diag and abs(pH[0]-pT[0]) == 1 and abs(pH[1]-pT[1]) == 1:
            return True
        return False

    @staticmethod
    def _update_tail(pH, pT):
        if Day09._is_close(pH, pT, include_diag=True):
            return pT
        quick_wins = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        for qw in quick_wins:
            pT_n = Day09._t_add(pT, qw)
            if Day09._is_close(pH, pT_n):
                return pT_n
        diags = [(-1,-1), (1, -1), (1, 1), (-1, 1)]
        for d in diags:
            pT_n = Day09._t_add (pT, d)
            if Day09._is_close(pH, pT_n, include_diag=True):
                return pT_n
        raise RuntimeError("Unexpeted State")

    def solve_1(self):
        pH = (0,0)
        pT = (0,0)
        visited_t = set()
        visited_t.add(pT)
        for move in self._moves:
            d,_n = move.split(" ")
            n = int(_n)
            m = (0,0)
            if d == 'R':
                m = (1,0)
            elif d == 'L':
                m = (-1, 0)
            elif d == 'U':
                m = (0, -1)
            elif d == 'D':
                m = (0, 1)
            else:
                raise ValueError("Unexpected direction")
            for i in range(n):
                pH = Day09._t_add(pH, m)
                pT = Day09._update_tail(pH, pT)
                visited_t.add(pT)
        return len(visited_t)

    def solve_2(self):
        knots = [(0,0) for _ in range(10)]
        visited_t = set()
        visited_t.add((0,0))
        for move in self._moves:
            d, _n = move.split(" ")
            n = int(_n)
            m = (0, 0)
            if d == 'R':
                m = (1, 0)
            elif d == 'L':
                m = (-1, 0)
            elif d == 'U':
                m = (0, -1)
            elif d == 'D':
                m = (0, 1)
            else:
                raise ValueError("Unexpected direction")
            for i in range(n):
                knots[0] = Day09._t_add(knots[0],m)
                for i in range(1, len(knots)):
                    knots[i] = Day09._update_tail(knots[i-1], knots[i])
                visited_t.add(knots[-1])
        return len(visited_t)
