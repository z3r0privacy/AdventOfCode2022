from aoc2022.day import Day
import math

class Day11 (Day):
    class Monkey:
        def __init__(self, init_items, operation, test, m_true, m_false) -> None:
            self._items = init_items
            self._operation = operation
            self._test = test
            self._m_true = m_true
            self._m_false = m_false
            self._insptect_count = 0

        @property
        def inspect_count(self):
            return self._insptect_count

        def play_round(self, all_monkeys, mod, div=3):
            for i in self._items:
                i = self._operation(i)
                i = int(i/div)
                i = i%mod
                if self._test(i):
                    all_monkeys[self._m_true]._items.append(i)
                else:
                    all_monkeys[self._m_false]._items.append(i)
                self._insptect_count += 1
            self._items = []

    def __init__(self):
        super().__init__(__name__)
        self._isdone = True
        self._content = self.read_file()

    @staticmethod
    def _add(old, a, b):
        _a = a if a is not None else old
        _b = b if b is not None else b
        return _a + _b

    @staticmethod
    def _mult(old, a, b):
        _a = a if a is not None else old
        _b = b if b is not None else old
        return _a * _b

    @staticmethod
    def _init_monkeys(content):
        monkey_strs = content.split("\n\n")
        monkeys = []
        the_mod = 1
        for ms in monkey_strs:
            data = ms.split("\n")
            items_raw = data[1].split(": ")[1].split(", ")
            items = [int(i) for i in items_raw]
            raw_op = data[2].split("= ")[1].split(" ")
            op_a = int(raw_op[0]) if raw_op[0].isnumeric() else None
            op_b = int(raw_op[2]) if raw_op[2].isnumeric() else None
            if raw_op[1] == "+":
                op = lambda item, op_a=op_a, op_b=op_b: Day11._add(item, op_a, op_b)
            elif raw_op[1] == "*":
                op = lambda item, op_a=op_a,op_b=op_b: Day11._mult(item, op_a, op_b)
            else:
                raise RuntimeError("Illegal operation")
            test_raw = int(data[3].split(": ")[1].split(" ")[2])
            test = lambda item, test_raw=test_raw: item%test_raw == 0
            the_mod *= test_raw
            m_true = int(data[4].split(" ")[-1])
            m_false = int(data[5].split(" ")[-1])
            m = Day11.Monkey(items, op, test, m_true, m_false)
            monkeys.append(m)
        return monkeys, the_mod

    def solve_1(self):
        monkeys, mod = Day11._init_monkeys(self._content)
        for i in range(20):
            for m in monkeys:
                m.play_round(monkeys, mod=mod, div=3)
        mbs = [m.inspect_count for m in monkeys]
        mbs.sort(reverse=True)
        return mbs[0]*mbs[1]

    def solve_2(self):
        monkeys, mod = Day11._init_monkeys(self._content)
        for i in range(10000):
            for m in monkeys:
                m.play_round(monkeys, mod=mod, div=1)
        mbs = [m.inspect_count for m in monkeys]
        mbs.sort(reverse=True)
        return mbs[0]*mbs[1]