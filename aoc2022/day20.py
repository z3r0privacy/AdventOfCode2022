from aoc2022.day import Day

class Day20 (Day):
    class LLElem:
        def __init__(self, value, pre, after) -> None:
            self.value = value
            self.pre = pre
            self.after = after

        def move_left(self, amount):
            if amount == 0:
                return
            self.pre.after = self.after
            self.after.pre = self.pre
            new_pre = self.pre
            for _ in range(amount):
                new_pre = new_pre.pre
            new_after = new_pre.after
            new_pre.after = self
            self.pre = new_pre
            new_after.pre = self
            self.after = new_after

        def move_right(self, amount):
            if amount == 0:
                return
            self.pre.after = self.after
            self.after.pre = self.pre
            new_after = self.after
            for _ in range(amount):
                new_after = new_after.after
            new_pre = new_after.pre
            new_pre.after = self
            self.pre = new_pre
            new_after.pre = self
            self.after = new_after

        def move(self, amount):
            if amount < 0:
                self.move_left(abs(amount))
            else:
                self.move_right(amount)

    def __init__(self):
        super().__init__(__name__)
        self._isdone = True
        self._numbers = self.read_file_lines_as_num()

    def solve_1(self):
        elements = [Day20.LLElem(nr, None, None) for nr in self._numbers]
        zero_value = None
        for i in range(len(elements)):
            elements[i].pre = elements[(i-1)%len(elements)]
            elements[i].after = elements[(i+1)%len(elements)]
            if elements[i].value == 0:
                zero_value = elements[i]
        for el in elements:
            el.move(el.value)
        curr_eval = zero_value
        sum = 0
        for i in range(3000):
            curr_eval = curr_eval.after
            if (i+1)%1000 == 0:
                sum += curr_eval.value
        return sum


    def solve_2(self):
        # takes a few seconds, too long to wait
        return "14579387544492 (Cached)"
        elements = [Day20.LLElem(nr*811589153, None, None) for nr in self._numbers]
        zero_value = None
        for i in range(len(elements)):
            elements[i].pre = elements[(i-1)%len(elements)]
            elements[i].after = elements[(i+1)%len(elements)]
            if elements[i].value == 0:
                zero_value = elements[i]
        for _ in range(10):
            for el in elements:
                el.move(el.value%(len(elements)-1))
        curr_eval = zero_value
        sum = 0
        for i in range(3000):
            curr_eval = curr_eval.after
            if (i+1)%1000 == 0:
                sum += curr_eval.value
        return sum