from aoc2022.day import Day
import math

class Day19_21 (Day):

    class Scanner:

        rots = [
            lambda x,y,z: (x,y,z),
            lambda x,y,z: (z, y, -x),
            lambda x,y,z: (-x, y, -z),
            lambda x,y,z: (-z, y, x)
        ]
        base_rotations = [
            # y up ("normal")
            lambda x,y,z: (x,y,z),
            #lambda x,y,z: (z,y,-x),
            #lambda x,y,z: (-x, y, -z),
            #lambda x,y,z: (-z, y, x)

            # -y up
            lambda x,y,z: (x, -y, -z),
            #lambda x,y,z: (z, -y, x),
            #lambda x,y,z: (-x, -y, z),
            #lambda x,y,z: (-z, -y, -x),

            # x up
            lambda x,y,z: (y, -x, z),

            # -x up
            lambda x,y,z: (-y, x, z),

            # z up
            lambda x,y,z: (x, -z, y),

            # -z up
            lambda x,y,z: (x, z, -y)
        ]
        num_rotations = 24

        def __init__(self, id) -> None:
            self.raw_beacons = []
            self.fixed_location = None
            self.fixed_rotation = None
            self.id = id
            self.not_matching_ids = []

        def add_raw_beacon(self, x,y,z):
            self.raw_beacons.append((x,y,z))

        def get_rotated_beacons(self, rotate):
            base = int(rotate / 4)
            rot = rotate % 4
            return [Day19_21.Scanner.rots[rot](*Day19_21.Scanner.base_rotations[base](*axis)) for axis in self.raw_beacons]

        def get_fixed_beacons(self):
            if self.fixed_location is None or self.fixed_rotation is None:
                return []
            rot_beac = self.get_rotated_beacons(self.fixed_rotation)
            xs, ys, zs = self.fixed_location
            return [(x+xs, y+ys, z+zs) for (x,y,z) in rot_beac]

    def __init__(self):
        super().__init__(__name__)
        self._isdone = False
        self._lines = self.read_file_lines()
        self.scanners = self._get_scanners()

    def _compare_two_beacon_sets(self, bs1, bs2):
        for anc1 in bs1:
            for anc2 in bs2:
                cnt = 1
                for c1 in bs1:
                    xd1 = c1[0] - anc1[0]
                    yd1 = c1[1] - anc1[1]
                    zd1 = c1[2] - anc1[2]
                    for c2 in bs2:
                        xd2 = c2[0] - anc2[0]
                        yd2 = c2[1] - anc2[1]
                        zd2 = c2[2] - anc2[2]
                        if xd1 == xd2 and yd1 == yd2 and zd1 == zd2:
                            cnt += 1
                if cnt >= 12:
                    return anc1, anc2
        return None

    def read_file_lines(self, strip=True):
        with open("Inputs/19_21.txt", "r") as f:
            return f.readlines()

    def _get_scanners(self):
        scanners = []
        cs = None
        id = 0
        for l in self._lines:
            if l.strip() == "":
                continue
            if l.startswith("---"):
                cs = Day19_21.Scanner(id)
                id += 1
                scanners.append(cs)
                continue
            x,y,z = l.split(",")
            cs.add_raw_beacon(int(x), int(y), int(z))
        scanners[0].fixed_rotation = 0
        scanners[0].fixed_location = (0,0,0)
        return scanners

    def solve_1(self):
        scanners = self.scanners
        #res = scanners[0].get_fixed_beacons()
        print("Got scanners, start searching and resolving")
        while any(s.fixed_location is None for s in scanners):
            for cs in [s for s in scanners if s.fixed_location is None]:
                for fs in [s for s in scanners if s.fixed_location is not None]:
                    if cs.fixed_location is not None:
                        # location has been found
                        break
                    if fs.id in cs.not_matching_ids:
                        # already tried, skipping
                        continue
                    bs_fixed = fs.get_fixed_beacons()
                    for r in range(24):
                        bs_candidate = cs.get_rotated_beacons(r)
                        res = self._compare_two_beacon_sets(bs_fixed, bs_candidate)
                        if res is not None:
                            fx = res[0][0] - res[1][0]
                            fy = res[0][1] - res[1][1]
                            fz = res[0][2] - res[1][2]
                            cs.fixed_location = (fx,fy,fz)
                            cs.fixed_rotation = r
                            print(f"Found Scanner {cs.id} at {(fx,fy,fz)} with rot {r}")
                            break
                    if cs.fixed_location is None:
                        cs.not_matching_ids.append(fs.id)
        beacons = set()
        for s in scanners:
            fb = s.get_fixed_beacons()
            for b in fb:
                beacons.add(b)
        return len(beacons)


    def solve_2(self):
        max_dist = 0
        for s1 in self.scanners:
            for s2 in self.scanners:
                xd = abs(s1.fixed_location[0] - s2.fixed_location[0])
                yd = abs(s1.fixed_location[1] - s2.fixed_location[1])
                zd = abs(s1.fixed_location[2] - s2.fixed_location[2])
                s = xd+yd+zd
                if s > max_dist:
                    max_dist = s
        return max_dist