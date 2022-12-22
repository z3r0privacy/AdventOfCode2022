from aoc2022.day import Day

class Day22 (Day):
    def __init__(self):
        super().__init__(__name__)
        self._isdone = True
        input = self.read_file().split("\n\n")
        self._instr = input[1]
        self._map = self._create_map(input[0].split("\n"))

    def _create_map(self, lines):
        max_x = max(len(l) for l in lines)
        m = []
        for l in lines:
            line = []
            for i,c in enumerate(l):
                if c == '#':
                    line.append(False)
                elif c == '.':
                    line.append(True)
                else:
                    line.append(None)
            line.extend([None for _ in range(max_x - i-1)])
            m.append(line)
        return m

    def _turn(self, cur_d, turn):
        if cur_d == (1,0):
            return (0,1) if turn == 'R' else (0,-1)
        if cur_d == (0,1):
            return (-1, 0) if turn == 'R' else (1,0)
        if cur_d == (-1, 0):
            return (0, -1) if turn == 'R' else (0, 1)
        if cur_d == (0, -1):
            return (1, 0) if turn == 'R' else (-1, 0)
        raise RuntimeError("Unexptected state")

    def _get_steps(self, instr_pos):
        end_pos = instr_pos
        while end_pos < len(self._instr) and self._instr[end_pos].isnumeric():
            end_pos += 1
        return end_pos, int(self._instr[instr_pos:end_pos])

    def _do_step(self, pos, dir):
        if self._map[pos[1]][pos[0]] != True:
            raise RuntimeError("Illegal state")
        
        max_x = len(self._map[0])
        max_y = len(self._map)
        n_pos = ((pos[0]+dir[0])%max_x, (pos[1]+dir[1])%max_y)
        while self._map[n_pos[1]][n_pos[0]] is None:
            n_pos = ((n_pos[0]+dir[0])%max_x, (n_pos[1]+dir[1])%max_y)
        if self._map[n_pos[1]][n_pos[0]] == True:
            return n_pos
        if self._map[n_pos[1]][n_pos[0]] == False:
            return pos

    def _do_step_2(self, pos, dir):
        pos_r, dir_r = self._do_step_2_int(pos, dir)
        if self._map[pos_r[1]][pos_r[0]] == True:
            return pos_r, dir_r
        if self._map[pos_r[1]][pos_r[0]] == False:
            return pos, dir
        raise RuntimeError("illegal state")

    def _do_step_2_int(self, pos, dir):
        n_pos = ((pos[0]+dir[0]), (pos[1]+dir[1]))
        if n_pos[0] >= 0 and n_pos[0] < len(self._map[0]) and n_pos[1] >= 0 and n_pos[1] < len(self._map):
            if self._map[n_pos[1]][n_pos[0]] is not None:
                return n_pos,dir

        if pos[1] == 0 and dir == (0, -1):
            if pos[0] < 100:
                return (0, pos[0]+100), (1,0)
            return (pos[0]-100, 199), (0, -1)

        if pos[1] < 50 and (dir == (-1,0) or dir == (1,0)):
            if pos[0] == 50 and dir == (-1,0):
                return (0, 149-pos[1]), (1,0)
            if pos[0] == 149 and dir == (1,0):
                return (99, 149-pos[1]), (-1, 0)

        if pos[1] == 49 and dir == (0,1):
            return (99, pos[0]-50), (-1, 0)

        if pos[1] < 100:
            if pos[0] == 50 and dir == (-1,0):
                return (pos[1]-50, 100), (0,1)
            if pos[0] == 99 and dir == (1,0):
                return (pos[1]+50, 49), (0,-1)

        if pos[1] == 100 and dir == (0,-1):
            return (50, pos[0]+50), (1,0)
        
        if pos[1] < 150:
            if pos[0] == 0 and dir == (-1,0):
                return (50, 149-pos[1]), (1,0)
            if pos[0] == 99 and dir == (1,0):
                return (149, 149-pos[1]), (-1, 0)

        if pos[1] == 149 and dir == (0, 1):
            return (49, pos[0]+100), (-1, 0)

        if pos[0] == 0 and dir == (-1, 0):
            return (pos[1]-100, 0), (0, 1)

        if pos[0] == 49 and dir == (1,0):
            return (pos[1]-100, 149), (0, -1)

        if pos[1] == 199 and dir == (0,1):
            return (pos[0]+100, 0), (0, 1)
        

        raise RuntimeError("unexpected state")
        
    def solve_1(self):
        x = -1
        for i in range(len(self._map[0])):
            if self._map[0][i] == True:
                x = i
                break
        cur_pos = (x,0)
        d = (1,0)
        instr_pos = 0

        while instr_pos < len(self._instr):
            instr_pos, steps = self._get_steps(instr_pos)
            for _ in range(steps):
                cur_pos = self._do_step(cur_pos, d)
            if instr_pos < len(self._instr):
                d = self._turn(d, self._instr[instr_pos])
                instr_pos += 1
        sum = 1000*(cur_pos[1]+1) + 4*(cur_pos[0]+1)
        if d == (0,1):
            sum += 1
        elif d == (-1,0):
            sum += 2
        elif d == (0,-1):
            sum += 3
        return sum

    def solve_2(self):
        x = -1
        for i in range(len(self._map[0])):
            if self._map[0][i] == True:
                x = i
                break
        cur_pos = (x,0)
        d = (1,0)
        instr_pos = 0

        while instr_pos < len(self._instr):
            instr_pos, steps = self._get_steps(instr_pos)
            for _ in range(steps):
                cur_pos, d = self._do_step_2(cur_pos, d)
            if instr_pos < len(self._instr):
                d = self._turn(d, self._instr[instr_pos])
                instr_pos += 1
        sum = 1000*(cur_pos[1]+1) + 4*(cur_pos[0]+1)
        if d == (0,1):
            sum += 1
        elif d == (-1,0):
            sum += 2
        elif d == (0,-1):
            sum += 3
        return sum