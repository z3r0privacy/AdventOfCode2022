from aoc2022.day import Day

class Day03 (Day):
    def __init__(self):
        super().__init__(__name__)
        self._isdone = True
        self._lines = self.read_file_lines()

    def _get_val(self, ch):
        if ch < ord('a'):
            return int(ch-ord('A')+27)
        return int(ch-ord('a')+1)

    def solve_1(self):
        items = ""
        for line in self._lines:
            half = int(len(line)/2)
            first = line[:half]
            second = line[half:]
            for c in first:
                if c in second:
                    items += c
                    break
        self._get_val(ord(items[0]))
        return sum([self._get_val(ord(c)) for c in items])

    def solve_2(self):
        badges = ""
        pos = 0
        while True:
            group = self._lines[pos:pos+3]
            if len(group) < 3:
                break
            for c in group[0]:
                if c in group[1] and c in group[2]:
                    badges += c
                    break
            pos += 3
        return sum(self._get_val(ord(c)) for c in badges)