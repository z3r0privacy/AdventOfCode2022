from day import Day

class Day02 (Day):
    def __init__(self):
        super().__init__(__name__)
        self._isdone = True
        self.strategy = self.read_file_lines()
        self.hands = {
            'A': ('R', 1),
            'B': ('P', 2),
            'C': ('S', 3)
        }

    def _me_points(self, opp, me):
        if opp[0] == me[0]:
            return 3
        if opp[0] == 'R':
            if me[0] == 'P':
                return 6
            return 0
        if opp[0] == 'P':
            if me[0] == 'R':
                return 0
            return 6
        if me[0] == 'P':
            return 0
        return 6

    def _me_chose(self, opp, res):
        if res == 'Y':
            return self.hands[opp]
        if res == 'X':
            if opp == 'A':
                return self.hands['C']
            if opp == 'B':
                return self.hands['A']
            return self.hands['B']
        if opp == 'A':
            return self.hands['B']
        if opp == 'B':
            return self.hands['C']
        return self.hands['A']

    def solve_1(self):
        hands = self.hands
        hands['X'] = hands['A']
        hands['Y'] = hands['B']
        hands['Z'] = hands['C']

        points = 0
        for l in self.strategy:
            opp, me = l.split(" ")
            opp = hands[opp]
            me = hands[me]
            points += me[1]
            points += self._me_points(opp, me)
        return points

    def solve_2(self):
        hands = self.hands
        hands['X'] = hands['A']
        hands['Y'] = hands['B']
        hands['Z'] = hands['C']

        points = 0
        for l in self.strategy:
            opp, res = l.split(" ")
            me = self._me_chose(opp, res)
            opp = hands[opp]
            points += me[1]
            points += self._me_points(opp, me)
        return points