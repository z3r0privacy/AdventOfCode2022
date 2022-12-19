from aoc2022.day import Day

class Day14 (Day):
    def __init__(self):
        super().__init__(__name__)
        self._isdone = True
        self._paths = self.read_file_lines()

    def _create_paths(self):
        field = set()
        lowest_y = 0
        for l in self._paths:
            coords = l.split(" -> ")
            for i in range(1, len(coords)):
                x1,y1 = [int(n) for n in coords[i-1].split(",")]
                x2,y2 = [int(n) for n in coords[i].split(",")]
                xs = -1 if x2 < x1 else (0 if x1 == x2 else 1)
                ys = -1 if y2 < y1 else (0 if y1 == y2 else 1)
                my = max(y1,y2)
                if my > lowest_y:
                    lowest_y = my
                for i in range(abs(x1-x2)+abs(y1-y2)+1):
                    field.add((x1,y1))
                    x1 += xs
                    y1 += ys
        return field, lowest_y

    @staticmethod
    def print_map(orig, now):
        for y in range(0, 10):
            l = ""
            for x in range(490, 510):
                p = (x,y)
                if p in now:
                    if p in orig:
                        l += '#'
                    else:
                        l += "o"
                else:
                    l += ' '
            print(l)

    def solve_1(self):
        occ, low_y = self._create_paths()
        cnt_sand = 0
        s_moves = [(0,1), (-1,1), (1,1)]
        while True:
            s_x = 500
            s_y = 0
            moved = True
            while moved:
                moved = False
                for xs, ys in s_moves:
                    if (s_x+xs, s_y+ys) not in occ:
                        moved = True
                        s_x += xs
                        s_y += ys
                        break
                if s_y > low_y:
                    return cnt_sand
            occ.add((s_x,s_y))
            cnt_sand += 1

    def solve_2(self):
        occ, low_y = self._create_paths()
        cnt_sand = 0
        s_moves = [(0,1), (-1,1), (1,1)]
        while True:
            s_x = 500
            s_y = 0
            moved = True
            while moved:
                moved = False
                for xs, ys in s_moves:
                    if (s_x+xs, s_y+ys) not in occ and (s_y+ys)<(low_y+2):
                        moved = True
                        s_x += xs
                        s_y += ys
                        break
            occ.add((s_x,s_y))
            cnt_sand += 1
            if s_x == 500 and s_y == 0:
                return cnt_sand