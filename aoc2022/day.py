import os

class Day:
    def __init__(self, name):
        self._day = name[-2:]
        self._isdone = False

    @property
    def Day(self):
        return self._day

    @property
    def Done(self):
        return self._isdone

    def solve_1(self):
        return "Not yet implemented"

    def solve_2(self):
        return "Not yet implemented"


    def read_file(self):
        path = os.path.join("Inputs", f"{self.Day}.txt")
        with open(path, "r") as f:
            return f.read()

    def read_file_lines(self):
        path = os.path.join("Inputs", f"{self.Day}.txt")
        with open(path, "r") as f:
            lines = [l.strip() for l in f.readlines()]
            while not lines[-1]:
                lines = lines[:-1]
            return lines

    def read_file_lines_as_num(self):
        return [int(l) for l in self.read_file_lines() if l]


