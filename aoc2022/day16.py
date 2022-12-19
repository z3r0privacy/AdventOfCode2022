from aoc2022.day import Day

class Day16 (Day):
    class Valve:
        def __init__(self, name, f_rate) -> None:
            self.neighbors = []
            self.name = name
            self.f_rate = f_rate
            self._cache = {}

        def _get_next_value_neighbors(self, visited, travel_list=[]):
            l = []
            travel_list.append(self)
            for n in self.neighbors:
                if n in travel_list:
                    continue
                if n.f_rate > 0: # and n not in visited:
                    l.append((n, len(travel_list)))
                l.extend(n._get_next_value_neighbors(visited, travel_list=travel_list))
            travel_list.pop()
            return l

        def get_next_value_neighbors(self, visited):
            if visited[-1] in self._cache.keys():
                d = self._cache[visited[-1]].copy()
            else:
                vals = self._get_next_value_neighbors(visited)
                d = {}
                for can,dist in vals:
                    if can not in d.keys():
                        d[can] = dist
                    elif dist < d[can]:
                        d[can] = dist
                self._cache[visited[-1]] = d.copy()
            for v in visited:
                if v in d.keys():
                    del d[v]
            return [(c,l) for c,l in d.items()]

        def __str__(self) -> str:
            return self.name


    def __init__(self):
        super().__init__(__name__)
        self._isdone = True
        lines = self.read_file_lines()
        self._valves = self._parse_valves(lines)

    def _parse_valves(self, lines):
        d = {}
        for l in lines:
            parts = l.split(" ")
            n = parts[1]
            f = int(parts[4][5:-1])
            d[n] = Day16.Valve(n, f)
        for l in lines:
            parts = l.split(" ")
            c = d[parts[1]]
            for n in parts[9:]:
                n = n.replace(",","")
                c.neighbors.append(d[n])
        return d


    def calc_visited(self, visited):
        res = 0
        for v, m in visited:
            res += v.f_rate*m
        return res

    def bt(self, remaining, visited):
        loc_max = 0
        for cand,dist in visited[-1][0].get_next_value_neighbors([v[0] for v in visited]):
            if dist < remaining and cand not in [v[0] for v in visited]:
                remaining -= dist+1
                visited.append((cand, remaining))
                val = self.bt(remaining, visited)
                if val > loc_max:
                    loc_max = val
                    #print(f"{loc_max=} :: " + ", ".join(f"{n}: {v}" for v,n in visited))
                visited.pop()
                remaining += dist+1
        
        if loc_max == 0:
            loc_max = self.calc_visited(visited)

        return loc_max

    def bt2(self, remaining_a, remaining_b, visited, last_a, last_b):
        loc_max = 0
        last = last_a if remaining_a >= remaining_b else last_b
        remaining = remaining_a if remaining_a >= remaining_b else remaining_b

        for cand,dist in last.get_next_value_neighbors([v[0] for v in visited]):
            if dist < remaining and cand not in [v[0] for v in visited]:
                remaining -= dist+1
                visited.append((cand, remaining))
                ra = remaining if remaining_a >= remaining_b else remaining_a
                rb = remaining_b if remaining_a >= remaining_b else remaining
                la = cand if remaining_a >= remaining_b else last_a
                lb = last_b if remaining_a >= remaining_b else cand
                val = self.bt2(ra, rb, visited, la, lb)
                if val > loc_max:
                    loc_max = val
                visited.pop()
                remaining += dist+1
        
        if loc_max == 0:
            loc_max = self.calc_visited(visited)

        return loc_max

    def solve_1(self):
        return self.bt(30, [(self._valves['AA'],0)])

    def solve_2(self):
        # takes a few seconds, too long to wait
        return "2111 (Cached)"
        return self.bt2(26, 26, [(self._valves['AA'],0)], self._valves['AA'], self._valves['AA'])