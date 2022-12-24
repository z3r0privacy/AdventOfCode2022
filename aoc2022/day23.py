from aoc2022.day import Day

class Day23 (Day):
    def __init__(self):
        super().__init__(__name__)
        self._isdone = True
        self._input_lines = self.read_file_lines()
        self._directions = [
            [(0, -1), (-1, -1), (1, -1)],
            [(0, 1), (-1, 1), (1, 1)],
            [(-1, 0), (-1, -1), (-1, 1)],
            [(1, 0), (1, -1), (1, 1)]
        ]

    def _create_elves_map(self) -> list[tuple[int,int]]:
        elves_pos = []
        for y,l in enumerate(self._input_lines):
            for x,c in enumerate(l):
                if c == '#':
                    elves_pos.append((x,y))
        return elves_pos

    def solve_1(self):
        elves_pos = self._create_elves_map()
        direction_index = 0
        for _ in range(10):
            proposed:dict[tuple[int,int],int] = {}
            elve_proposal = []
            pos_set = set(elves_pos)
            # calc proposals
            for e in elves_pos:
                is_free = True
                for adj in [(-1,-1), (0,-1), (1,-1), (1,0), (1,1), (0,1), (-1,1), (-1, 0)]:
                    if (e[0]+adj[0], e[1]+adj[1]) in pos_set:
                        is_free = False
                        break
                if is_free:
                    elve_proposal.append(None)
                    continue
                # check directions
                proposal = None
                for i in range(4):
                    curr_elve_dir = (direction_index+i)%4
                    is_free = True
                    for adj in self._directions[curr_elve_dir]:
                        if (e[0]+adj[0], e[1]+adj[1]) in pos_set:
                            is_free = False
                            break
                    if is_free:
                        proposal = (e[0]+self._directions[curr_elve_dir][0][0], e[1]+self._directions[curr_elve_dir][0][1])
                        break
                if proposal is not None:
                    if proposal not in proposed.keys():
                        proposed[proposal] = 0
                    proposed[proposal] += 1
                elve_proposal.append(proposal)
            # do moves
            for i,prop in enumerate(elve_proposal):
                if prop is None:
                    continue
                if proposed[prop] > 1:
                    continue
                elves_pos[i] = prop
            direction_index += 1
        
        min_x = max_x = min_y = max_y = None
        for x,y in elves_pos:
            if min_x is None or min_x > x:
                min_x = x
            if max_x is None or max_x < x:
                max_x = x
            if min_y is None or min_y > y:
                min_y = y
            if max_y is None or max_y < y:
                max_y = y
        area = (max_x-min_x+1)*(max_y-min_y+1)
        return area - len(elves_pos)
                


    def solve_2(self):
        return "881 (Cached)"
        elves_pos = self._create_elves_map()
        direction_index = 0
        while True:
            proposed:dict[tuple[int,int],int] = {}
            elve_proposal = []
            pos_set = set(elves_pos)
            # calc proposals
            for e in elves_pos:
                is_free = True
                for adj in [(-1,-1), (0,-1), (1,-1), (1,0), (1,1), (0,1), (-1,1), (-1, 0)]:
                    if (e[0]+adj[0], e[1]+adj[1]) in pos_set:
                        is_free = False
                        break
                if is_free:
                    elve_proposal.append(None)
                    continue
                # check directions
                proposal = None
                for i in range(4):
                    curr_elve_dir = (direction_index+i)%4
                    is_free = True
                    for adj in self._directions[curr_elve_dir]:
                        if (e[0]+adj[0], e[1]+adj[1]) in pos_set:
                            is_free = False
                            break
                    if is_free:
                        proposal = (e[0]+self._directions[curr_elve_dir][0][0], e[1]+self._directions[curr_elve_dir][0][1])
                        break
                if proposal is not None:
                    if proposal not in proposed.keys():
                        proposed[proposal] = 0
                    proposed[proposal] += 1
                elve_proposal.append(proposal)
            # do moves
            num_moves = 0
            for i,prop in enumerate(elve_proposal):
                if prop is None:
                    continue
                if proposed[prop] > 1:
                    continue
                elves_pos[i] = prop
                num_moves += 1
            direction_index += 1
            if num_moves == 0:
                return direction_index
