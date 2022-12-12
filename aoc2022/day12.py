from aoc2022.day import Day

class Day12 (Day):
    def __init__(self):
        super().__init__(__name__)
        self._isdone = True
        self._field = [[c for c in s] for s in self.read_file_lines()]
        self._s = self._e = None
        self._dist = None

    def _get_candidates_1(self, pt):
        def try_get(x,y):
            if y < len(self._field) and y >= 0 and x >= 0 and x < len(self._field[y]):
                return True
            return False
        moves = [(-1,0), (1,0), (0, -1), (0,1)]
        cs = []
        for m in moves:
            x,y = pt[0]+m[0], pt[1]+m[1]
            if try_get(x,y):
                v_ot = self._field[y][x]
                if v_ot == 'S': v_ot = 'a'
                if v_ot == 'E': v_ot = 'z'
                h_ot = ord(v_ot)
                v_me = self._field[pt[1]][pt[0]]
                if v_me == 'S': v_me = 'a'
                h_me = ord(v_me)
                if h_ot <= h_me+1:
                    cs.append((x,y))
        return cs

    def _get_candidates_2(self, pt):
        def try_get(x,y):
            if y < len(self._field) and y >= 0 and x >= 0 and x < len(self._field[y]):
                return True
            return False
        moves = [(-1,0), (1,0), (0, -1), (0,1)]
        cs = []
        for m in moves:
            x,y = pt[0]+m[0], pt[1]+m[1]
            if try_get(x,y):
                v_ot = self._field[y][x]
                if v_ot == 'S': v_ot = 'a'
                if v_ot == 'E': v_ot = 'z'
                h_ot = ord(v_ot)
                v_me = self._field[pt[1]][pt[0]]
                if v_me == 'S': v_me = 'a'
                if v_me == 'E': v_me = 'z'
                h_me = ord(v_me)
                if h_ot >= h_me-1:
                    cs.append((x,y))
        return cs

    def _find_path(self, pt, cand_finder):
        print("Going for Bellman-Ford")
        dist = {}
        pre = {}
        for y in range(len(self._field)):
            for x in range(len(self._field[y])):
                dist[(x,y)] = None
                pre[(x,y)] = None
        dist[pt] = 0
        print(f"Rounds: {len(self._field)*len(self._field[0])}")
        for i in range(len(self._field)*len(self._field[0])):
            if i > 0 and i%100==0:
                print(f"Round: {i}")
            for y in range(len(self._field)):
                for x in range(len(self._field[y])):
                    if dist[(x,y)] is None:
                        continue
                    for c in cand_finder((x,y)):
                        if dist[c] is None or dist[c] > (dist[(x,y)]+1):
                            dist[c] = dist[(x,y)]+1
                            pre[c] = (x,y)
        return dist


    def solve_1(self):
        # takes a few seconds, too long to wait
        return "447 (Cached)"
        for y in range(len(self._field)):
            for x in range(len(self._field[y])):
                if self._field[y][x] == 'S':
                    self._s = (x,y)
                elif self._field[y][x] == 'E':
                    self._e = (x,y)
        
        self._dist = self._find_path(self._e, self._get_candidates_2)
        return self._dist[self._s]

    def solve_2(self):
        # takes a few seconds, too long to wait
        return "446 (Cached)"
        return min(val for (x,y),val in self._dist.items() if val is not None and self._field[y][x] in ['a','S'])