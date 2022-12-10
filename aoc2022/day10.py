from aoc2022.day import Day

class Day10 (Day):
    class Instruction:
        def __init__(self, n_cylces) -> None:
            self._n_cycles = n_cylces
            self._curr_cycle = 0

        def do_cycle(self, state):
            self._curr_cycle += 1
            pass

        def is_finished(self):
            return self._curr_cycle == self._n_cycles

        @staticmethod
        def parse_instruction(instr:str) -> "Day10.Instruction":
            if instr.startswith("noop"):
                return Day10.InstrNoop()
            elif instr.startswith("addx"):
                return Day10.InstrAddx(int(instr.split(" ")[1]))

    class InstrNoop(Instruction):
        def __init__(self) -> None:
            super().__init__(1)

    class InstrAddx(Instruction):
        def __init__(self, value) -> None:
            super().__init__(2)
            self._value = value

        def do_cycle(self, state):
            self._curr_cycle += 1
            if self._curr_cycle == 2:
                state['X'] += self._value

    def __init__(self):
        super().__init__(__name__)
        self._isdone = True
        self._instrs = self.read_file_lines()

    def solve_1(self):
        instrs = [Day10.Instruction.parse_instruction(i) for i in self._instrs]
        # to use it as stack
        instrs.reverse()
        cycle = 0
        state = {
            'X': 1
        }
        sig_strength = 0
        curr_instr = instrs.pop()
        while len(instrs) > 0:
            cycle += 1
            if curr_instr.is_finished():
                curr_instr = instrs.pop()
            if cycle == 20 or (cycle-20)%40 == 0:
                sig_strength += cycle*state['X']
            curr_instr.do_cycle(state)
        return sig_strength

    def solve_2(self):
        instrs = [Day10.Instruction.parse_instruction(i) for i in self._instrs]
        # to use it as stack
        instrs.reverse()
        cycle = 0
        state = {
            'X': 1
        }
        screen = ""
        curr_instr = instrs.pop()
        while len(instrs) > 0:
            if curr_instr.is_finished():
                curr_instr = instrs.pop()
            pos = cycle%40
            if pos-1 == state['X'] or pos == state['X'] or pos+1==state['X']:
                screen += '#'
            else:
                screen += '.'
            cycle += 1
            curr_instr.do_cycle(state)
        for i in range(0, len(screen), 40):
            # for solving, print the lines to see output
            # print(screen[i:i+40])
            pass
        return "EFUGLPAP"