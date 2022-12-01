from day import Day
import aocutils

class Day01 (Day):
    def __init__(self):
        super().__init__(__name__)
        self._isdone = True
        self.lines = self.read_file_lines()
        self.elves = []

    def solve_1(self):
        current_elve = 0
        for l in self.lines:
            if l == "" and current_elve > 0:
                self.elves.append(current_elve)
                current_elve = 0
            else:
                current_elve += int(l)
        if current_elve > 0:
            self.elves.append(current_elve)
        self.elves.sort(reverse=True)
        return self.elves[0]

    def solve_2(self):
        return sum(self.elves[0:3])
        