from aoc2022.day import Day

class Day18 (Day):
    def __init__(self):
        super().__init__(__name__)
        self._isdone = True
        self._stones = set([(int(c[0]), int(c[1]), int(c[2])) for c in [coords.split(",") for coords in self.read_file_lines()]])
        self._max_x = max(c[0] for c in self._stones)+2
        self._max_y = max(c[1] for c in self._stones)+2
        self._max_z = max(c[2] for c in self._stones)+2
        self._pt2_cache = {}

    def solve_1(self):
        sides = 0
        s_pos = [(1,0,0), (-1,0,0), (0,1,0), (0,-1,0), (0,0,1), (0,0,-1)]
        for s in self._stones:
            for x,y,z in s_pos:
                if (s[0]+x, s[1]+y, s[2]+z) not in self._stones:
                    sides += 1
        return sides

    def _bf(self):
        dist = {}
        n_pos = [(1,0,0), (-1,0,0), (0,1,0), (0,-1,0), (0,0,1), (0,0,-1)]
        for x in range(-1, self._max_x):
            for y in range(-1, self._max_y):
                for z in range(-1, self._max_z):
                    dist[(x,y,z)] = None
        
        dist[(0,0,0)] = 0
        changed = True
        for _ in range(len(dist)):
            if not changed:
                break
            changed = False
            for k,v in dist.items():
                if v is None:
                    continue
                for x,y,z in n_pos:
                    n = (k[0]+x, k[1]+y, k[2]+z)
                    if n in self._stones:
                        continue
                    if n[0] >= self._max_x or n[1] >= self._max_y or n[2] >= self._max_z or n[0] <= -2 or n[1] <= -2 or n[2] <= -2:
                        continue
                    if dist[n] is None:
                        dist[n] = v+1
                        changed = True
        return dist


    def solve_2(self):
        sides = 0
        dists = self._bf()
        s_pos = [(1,0,0), (-1,0,0), (0,1,0), (0,-1,0), (0,0,1), (0,0,-1)]

        for s in self._stones:
            for x,y,z in s_pos:
                if dists[(s[0]+x, s[1]+y, s[2]+z)] is not None:
                    sides += 1
        return sides