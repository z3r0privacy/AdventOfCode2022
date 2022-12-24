from aoc2022.day import Day
from collections import deque

class Day24 (Day):
    def __init__(self):
        super().__init__(__name__)
        self._isdone = True
        self._lines = self.read_file_lines()
        self._best = None
        blizz_list = self._create_blizzard_list()
        self._blizz_lists = []
        self._blizz_lists.append(self._update_blizzlist(blizz_list))


    def _create_blizzard_list(self):
        blizz_list = []
        for y in range(len(self._lines)):
            for x in range(len(self._lines[y])):
                c = self._lines[y][x]
                if c in ['<', '>', 'v', '^']:
                    blizz_list.append((x, y, c))
        return blizz_list

    def _update_blizzlist(self, blizz_list):
        def move(x,y,c):
            if c == '<':
                x -= 1
                if x <= 0:
                    x = len(self._lines[y])-2
            elif c == '>':
                x += 1
                if x == len(self._lines[y])-1:
                    x = 1
            elif c == 'v':
                y += 1
                if y == len(self._lines)-1:
                    y = 1
            else:
                y -= 1
                if y <= 0:
                    y = len(self._lines)-1
            return x,y

        new_blizz_list = []
        for x,y,c in blizz_list:
            nx,ny = move(x,y,c)
            new_blizz_list.append((nx,ny,c))
        return new_blizz_list

    def _get_blizz(self, time):
        while time >= len(self._blizz_lists):
            self._blizz_lists.append(self._update_blizzlist(self._blizz_lists[-1]))
        return self._blizz_lists[time]

    def calc_state(self, time, c_pos, goal):
        if c_pos == goal:
            if self._best is None or time < self._best:
                # print(f"New best: {time} minutes")
                self._best = time
            return

        blizz_locs = set([(x,y) for x,y,_ in self._get_blizz(time)])
        newstates = []
        for mx,my in [(0,1), (1,0), (-1,0), (0,-1), (0,0)]:
            x,y = c_pos[0]+mx, c_pos[1]+my
            if y == goal[1] and x == goal[0]:
                # found goal, all other ways will be longer
                return [(time+1, (x,y), goal)]
            if y < 0 or y >= len(self._lines):
                continue
            if x < 0 or x >= len(self._lines[y]):
                continue
            if (x,y) in blizz_locs:
                continue
            if self._lines[y][x] == '#':
                continue
            newstates.append((time+1, (x,y), goal))
        return newstates

    def solve_1(self):
        return "225 (Cached)"
        self._goaly = len(self._lines)-1
        self._goalx = len(self._lines[self._goaly])-2
        
        states_seen = set()
        queue = deque()
        states_seen.add((0, (1,0), (self._goalx, self._goaly)))
        queue.append((0, (1,0), (self._goalx, self._goaly)))
        while len(queue):
            s = queue.popleft()
            newstates = self.calc_state(*s)
            if newstates is None:
                return self._best
            for ns in newstates:
                if ns not in states_seen:
                    states_seen.add(ns)
                    queue.append(ns)
                

    def solve_2(self):
        return "809 (Cached)"
        p1 = self._best
        self._best = None
        p2 = None

        states_seen = set()
        queue = deque()
        states_seen.add((p1, (self._goalx, self._goaly), (1,0)))
        queue.append((p1, (self._goalx, self._goaly), (1,0)))
        while len(queue):
            s = queue.popleft()
            newstates = self.calc_state(*s)
            if newstates is None:
                p2 = self._best
                self._best = None
                break
            for ns in newstates:
                if ns not in states_seen:
                    states_seen.add(ns)
                    queue.append(ns)

        states_seen = set()
        queue = deque()
        states_seen.add((p2, (1,0), (self._goalx, self._goaly)))
        queue.append((p2, (1,0), (self._goalx, self._goaly)))
        while len(queue):
            s = queue.popleft()
            newstates = self.calc_state(*s)
            if newstates is None:
                return self._best
            for ns in newstates:
                if ns not in states_seen:
                    states_seen.add(ns)
                    queue.append(ns)
        