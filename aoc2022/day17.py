from aoc2022.day import Day

class Day17 (Day):
    def __init__(self):
        super().__init__(__name__)
        self._isdone = True
        self._jet = self.read_file()
        

    def _next_rock(self, nr, height):
        nr = nr%5
        coords = []
        if nr == 0:
            coords = [(2,0), (3, 0), (4,0), (5,0)]
        elif nr == 1:
            coords = [(3,0), (2,1), (3,1), (4,1), (3,2)]
        elif nr == 2:
            coords = [(2,0), (3,0), (4,0), (4,1), (4,2)]
        elif nr == 3:
            coords = [(2,0), (2,1), (2,2), (2,3)]
        elif nr == 4:
            coords = [(2,0), (2,1), (3,0), (3,1)]
        else:
            raise RuntimeError("Illegal State")
        for i in range(len(coords)):
            coords[i] = (coords[i][0], coords[i][1]+height+4)
        return coords

    def _unapply(self, rock, move):
        for i in range(len(rock)):
            rock[i] = (rock[i][0]-move[0], rock[i][1]-move[1])

    def _apply_jet(self, rock, move_x, floor):
        for i in range(len(rock)):
            rock[i] = (rock[i][0]+move_x, rock[i][1])
        for r in rock:
            if r[0] < 0 or r[0] >= 7 or r in floor:
                self._unapply(rock, (move_x,0))
                return
    
    def _lower(self, rock, floor):
        for i in range(len(rock)):
            rock[i] = (rock[i][0], rock[i][1]-1)
        for r in rock:
            if r[1] < 0 or r in floor:
                self._unapply(rock, (0,-1))
                return False
        return True

    def solve_1(self):
        p_jet = 0
        height = -1
        rocks = 0
        floor = set()
        while rocks < 2022:
            rock = self._next_rock(rocks, height)
            while True:
                j = 1 if self._jet[p_jet] == '>' else -1
                p_jet = (p_jet+1)%len(self._jet)
                self._apply_jet(rock, j, floor)
                if not self._lower(rock, floor):
                    for r in rock:
                        floor.add(r)
                        if r[1] > height:
                            height = r[1]
                    rocks += 1
                    break
        return height+1


    def solve_2(self):
        p_jet = 0
        height = -1
        rocks = 0
        floor = set()
        repeated_patterns = []
        while True:
            if all((x,height) in floor for x in range(7)):
                repeated_patterns.append((rocks, rocks%5, height, p_jet))
                if len(repeated_patterns) == 2:
                    break
            rock = self._next_rock(rocks, height)
            while True:
                j = 1 if self._jet[p_jet] == '>' else -1
                p_jet = (p_jet+1)%len(self._jet)
                self._apply_jet(rock, j, floor)
                if not self._lower(rock, floor):
                    for r in rock:
                        floor.add(r)
                        if r[1] > height:
                            height = r[1]
                    rocks += 1
                    break

        d_rocks = repeated_patterns[1][0] - repeated_patterns[0][0]
        d_height = repeated_patterns[1][2] - repeated_patterns[0][2]
        remaining_rocks = 1000000000000-rocks
        mult = int(remaining_rocks/d_rocks)
        height += mult*d_height
        rocks += mult*d_rocks
        for x in range(7):
            floor.add((x, height))

        while rocks < 1000000000000:
            rock = self._next_rock(rocks, height)
            while True:
                j = 1 if self._jet[p_jet] == '>' else -1
                p_jet = (p_jet+1)%len(self._jet)
                self._apply_jet(rock, j, floor)
                if not self._lower(rock, floor):
                    for r in rock:
                        floor.add(r)
                        if r[1] > height:
                            height = r[1]
                    rocks += 1
                    break

        return height+1