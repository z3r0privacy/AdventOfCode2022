from aoc2022.day import Day

class Day08 (Day):
    def __init__(self):
        super().__init__(__name__)
        self._isdone = True
        input = self.read_file_lines()
        self._trees = [[int(x) for x in line] for line in input]

    def solve_1(self):
        cnt = 0
        for y in range(1, len(self._trees)-1):
            for x in range(1, len(self._trees[y])-1):
                val = self._trees[y][x]
                visible = True
                xs = x-1
                while xs >= 0:
                    if self._trees[y][xs] >= val:
                        visible = False
                        break
                    xs -= 1
                if visible:
                    cnt += 1
                    continue
                visible = True
                xs = x+1
                while xs < len(self._trees[y]):
                    if self._trees[y][xs] >= val:
                        visible = False
                        break
                    xs += 1
                if visible:
                    cnt += 1
                    continue

                visible = True
                ys = y-1
                while ys >= 0:
                    if self._trees[ys][x] >= val:
                        visible = False
                        break
                    ys -= 1
                if visible:
                    cnt += 1
                    continue
                visible = True
                ys = y+1
                while ys < len(self._trees):
                    if self._trees[ys][x] >= val:
                        visible = False
                        break
                    ys += 1
                if visible:
                    cnt += 1
                    continue
        return 2*len(self._trees) + 2*(len(self._trees[0])-2) + cnt
                


    def solve_2(self):
        curr_max = 0
        for y in range(1, len(self._trees)-1):
            for x in range(1, len(self._trees[y])-1):
                val = self._trees[y][x]
                left = 0
                xs = x
                while xs > 0:
                    xs -= 1
                    if self._trees[y][xs] >= val:
                        break
                left = abs(x-xs)
                
                right = 0
                xs = x
                while xs < len(self._trees[y])-1:
                    xs += 1
                    if self._trees[y][xs] >= val:
                        break
                right = abs(x-xs)

                top = 0
                ys = y
                while ys > 0:
                    ys -= 1
                    if self._trees[ys][x] >= val:
                        break
                top = abs(y-ys)

                down = 0
                ys = y
                while ys < len(self._trees)-1:
                    ys += 1
                    if self._trees[ys][x] >= val:
                        break
                down = abs(y-ys)

                res = left*right*top*down
                if res > curr_max:
                    curr_max = res
        return curr_max