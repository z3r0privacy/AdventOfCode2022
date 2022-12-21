from aoc2022.day import Day

class Day21 (Day):
    class Monkey:
        def __init__(self, name, value) -> None:
            self.name = name
            if value.isnumeric():
                self._is_num = True
                self.value = int(value)
            else:
                self._is_num = False
                self._left_monkey, self._op, self._right_monkey = value.split(" ")
        
        def get_value(self, all_monkeys):
            if self._is_num:
                return self.value
            ml = all_monkeys[self._left_monkey].get_value(all_monkeys)
            mr = all_monkeys[self._right_monkey].get_value(all_monkeys)
            if self._op == "+":
                return ml + mr
            elif self._op == "-":
                return ml - mr
            elif self._op == "*":
                return ml * mr
            elif self._op == "/":
                return int(ml / mr)
            raise RuntimeError("Invalid OP")

        def get_human(self, all_monkeys, expected):
            if self.name == "humn":
                return expected
            known = get = None
            ma = all_monkeys[self._left_monkey]
            mb = all_monkeys[self._right_monkey]
            known = ma if not ma._has_human(all_monkeys) else mb
            get = ma if known == mb else mb
            known_val = known.get_value(all_monkeys)
            if self.name == "root":
                return get.get_human(all_monkeys, known_val)
            elif self._op == "+":
                return get.get_human(all_monkeys, expected-known_val)
            elif self._op == "*":
                return get.get_human(all_monkeys, int(expected/known_val))
            elif self._op == "-":
                if get == ma:
                    return get.get_human(all_monkeys, expected+known_val)
                else:
                    return get.get_human(all_monkeys, -1*(expected-known_val))
            elif self._op == "/":
                if get == ma:
                    return get.get_human(all_monkeys, expected*known_val)
                else:
                    return get.get_human(all_monkeys, int(known_val/expected))
            raise RuntimeError("unexpected state")

        def _has_human(self, all_monkeys):
            if self.name == "humn":
                return True
            if self._is_num:
                return False
            return all_monkeys[self._left_monkey]._has_human(all_monkeys) or all_monkeys[self._right_monkey]._has_human(all_monkeys)

    def __init__(self):
        super().__init__(__name__)
        self._isdone = True
        self._lines = self.read_file_lines()


    def solve_1(self):
        monkeys = {}
        for l in self._lines:
            n,v = l.split(": ")
            monkeys[n] = Day21.Monkey(n, v)
        return monkeys["root"].get_value(monkeys)

    def solve_2(self):
        monkeys = {}
        for l in self._lines:
            n,v = l.split(": ")
            monkeys[n] = Day21.Monkey(n, v)
        return monkeys["root"].get_human(monkeys, None)