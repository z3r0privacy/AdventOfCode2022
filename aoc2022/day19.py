from aoc2022.day import Day
from math import ceil
from functools import reduce

class Day19 (Day):
    class BP:
        def __init__(self, ore_ore, clay_ore, obs_ore, obs_clay, geo_ore, geo_obs) -> None:
            self.ore_ore = ore_ore
            self.clay_ore = clay_ore
            self.obs_ore = obs_ore
            self.obs_clay = obs_clay
            self.geo_ore = geo_ore
            self.geo_obs = geo_obs

        def get_required_materials(self, robot):
            if robot == "ore":
                return {"ore":self.ore_ore}
            elif robot == "clay":
                return {"ore":self.clay_ore}
            elif robot == "obs":
                return {"ore": self.obs_ore, "clay": self.obs_clay}
            elif robot == "geo":
                return {"ore": self.geo_ore, "obs": self.geo_obs}
            raise RuntimeError("illegal robot type")

        def need_more(self, robot:str, robots:dict[str,int]):
            if robot == "ore":
                return robots["ore"] < max(self.ore_ore, self.clay_ore, self.obs_ore, self.geo_ore)
            elif robot == "clay":
                return robots["clay"] < self.obs_clay
            elif robot == "obs":
                return robots["obs"] < self.geo_obs
            return True

    def __init__(self):
        super().__init__(__name__)
        self._isdone = True
        bps_raw = [l.split(" ") for l in self.read_file_lines()]
        self._bps = [Day19.BP(int(w[6]), int(w[12]), int(w[18]), int(w[21]), int(w[27]), int(w[30])) for w in bps_raw]
        self._gm = 0
        self.num_minutes = 0

    def _can_reach_max(self, curr_min, num_geo_robots, curr_geo):
        n = self.num_minutes-curr_min+num_geo_robots
        sum = (n*(n+1)/2) - (num_geo_robots*(num_geo_robots-1)/2)
        return curr_geo+sum

    def _produce_neXt(self, bp:BP, curr_min:int, robots:dict[str,int], res:dict[str,int], next_robot:str):
        if curr_min >= self.num_minutes:
            if res['geo'] > self._gm:
                self._gm = res['geo']
            return res['geo']
        if next_robot == "obs" and robots["clay"] == 0:
            return 0
        if next_robot == "geo" and robots["obs"] == 0:
            return 0
        if not bp.need_more(next_robot, robots):
            return 0
        if self._can_reach_max(curr_min, robots['geo'], res['geo']) <= self._gm:
            #print("opt")
            return 0

        req = bp.get_required_materials(next_robot)
        dur_req = 0
        for k,v in req.items():
            diff = v - res[k]
            if diff > 0:
                mins = ceil(diff/robots[k])
                if mins > dur_req:
                    dur_req = mins
        dur = min(self.num_minutes-curr_min, dur_req)
        for k in res.keys():
            res[k] += dur * robots[k]
        curr_min += dur
        if curr_min >= self.num_minutes:
            if res['geo'] > self._gm:
                self._gm = res['geo']
            return res['geo']
        for k,v in req.items():
            res[k] -= v
        for k,v in robots.items():
            res[k] += v
        robots[next_robot] += 1
        curr_min += 1
        return max([
            self._produce_neXt(bp, curr_min, robots.copy(), res.copy(), "ore"),
            self._produce_neXt(bp, curr_min, robots.copy(), res.copy(), "clay"),
            self._produce_neXt(bp, curr_min, robots.copy(), res.copy(), "obs"),
            self._produce_neXt(bp, curr_min, robots.copy(), res.copy(), "geo"),
        ])

    def solve_1(self):
        # takes a few seconds, too long to wait
        return "1127 (Cached)"
        self.num_minutes = 24
        sum = 0
        for i,bp in enumerate(self._bps):
            self._gm = 0
            geo = max([
                self._produce_neXt(bp, 0, {"ore":1, "clay":0, "obs":0, "geo":0}, {"ore":0, "clay":0, "obs":0, "geo":0}, "ore"),
                self._produce_neXt(bp, 0, {"ore":1, "clay":0, "obs":0, "geo":0}, {"ore":0, "clay":0, "obs":0, "geo":0}, "clay"),
            ])
            # print(f"\n\n\n========== BP {i+1}: {geo} ==========\n\n\n")
            sum += (i+1) * geo
        return sum

    def solve_2(self):
        # takes a few seconds, too long to wait
        return "21546 (Cached)"
        self._gm = 0
        self.num_minutes = 32
        values = []
        for bp in self._bps[:3]:
            self._gm = 0
            geo = max([
                self._produce_neXt(bp, 0, {"ore":1, "clay":0, "obs":0, "geo":0}, {"ore":0, "clay":0, "obs":0, "geo":0}, "ore"),
                self._produce_neXt(bp, 0, {"ore":1, "clay":0, "obs":0, "geo":0}, {"ore":0, "clay":0, "obs":0, "geo":0}, "clay"),
            ])
            # print(f"\n\n\n========== BP: {geo} ==========\n\n\n")
            values.append(geo)
        return reduce(lambda a,b:a*b, values)