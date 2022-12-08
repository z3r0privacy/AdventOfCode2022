from aoc2022.day import Day

class Day06 (Day):
    def __init__(self):
        super().__init__(__name__)
        self._isdone = True
        self._content = self.read_file()

    def _is_different(self, s):
        for i in range(len(s)):
            for j in range(i+1, len(s)):
                if s[i] == s[j]:
                    return False
        return True

    def solve_1(self):
        i = 4
        while True:
            if self._is_different(self._content[i-4:i]):
                return i
            i += 1

    def solve_2(self):
        i = 14
        while True:
            if self._is_different(self._content[i-14:i]):
                return i
            i += 1