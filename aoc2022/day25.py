from aoc2022.day import Day

class Day25 (Day):
    def __init__(self):
        super().__init__(__name__)
        self._isdone = True
        self._lines  = self.read_file_lines()

    def _to_snafu(self, num):
        def get_range(pow):
            max = 0
            while pow > 0:
                max += 2*pow
                pow /= 5
            return -max, max
        pow = 1
        while int(num/pow) > 0:
            pow *= 5
        pow /= 5
        snafu = ""
        while pow > 0:
            min, max = get_range(pow/5)
            for v in range(-2,3):
                if min <= num - (v*pow) <= max:
                    num -= v*pow
                    pow = int(pow/5)
                    if v >= 0:
                        snafu += str(v)
                    elif v == -1:
                        snafu += "-"
                    elif v == -2:
                        snafu += "="
                    else:
                        raise RuntimeError()
                    break
        return snafu


    def solve_1(self):
        sum = 0
        for l in self._lines:
            curr_pow = 1
            for d in l[::-1]:
                v = -2
                if d == '-':
                    v = -1
                elif d.isnumeric():
                    v = int(d)
                sum += curr_pow*v
                curr_pow *= 5
        return self._to_snafu(sum)

    def solve_2(self):
        return "Started the Blender"