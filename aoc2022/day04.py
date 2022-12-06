from day import Day

class Day04 (Day):
    def __init__(self):
        super().__init__(__name__)
        self._isdone = True
        self._lines = self.read_file_lines()

    def _contains(self, it, other):
        return it[0] <= other[0] and it[1] >= other[1]

    def _overlap(self, r1, r2):
        def overlap_int(it, other):
            if it[0] <= other[0] and it[1] >= other[0]: return True
            if it[0] <= other[1] and it[1] >= other[1]: return True
            return False
        return overlap_int(r1,r2) or overlap_int(r2,r1)

    def solve_1(self):
        count = 0
        for l in self._lines:
            e1,e2 = l.split(",")
            r1 = [int(x) for x in e1.split("-")]
            r2 = [int(x) for x in e2.split("-")]
            if self._contains(r1,r2) or self._contains(r2,r1):
                count += 1
        return count

    def solve_2(self):
        count = 0
        for l in self._lines:
            e1,e2 = l.split(",")
            r1 = [int(x) for x in e1.split("-")]
            r2 = [int(x) for x in e2.split("-")]
            if self._overlap(r1,r2):
                count += 1
        return count