from day import Day

class Day05 (Day):
    def __init__(self):
        super().__init__(__name__)
        self._isdone = True
        input = self.read_file_lines()
        while input[0].strip() != "":
            input = input[1:]
        self._instr = input[1:]

    def _create_init_state(self) -> list[list[str]]:
        input = self.read_file_lines(strip=False)
        lines = []
        for l in input:
            if l.startswith(" 1"):
                break
            ldata = []
            i = 1
            while i < len(l):
                if l[i] == ' ':
                    ldata.append(None)
                else:
                    ldata.append(l[i])
                i += 4
            lines.append(ldata)
        lines.reverse()
        stacks = [[] for x in range(len(lines[0]))]
        for l in lines:
            for i in range(len(l)):
                if l[i]:
                    stacks[i].append(l[i])
        return stacks

    def solve_1(self):
        stacks = self._create_init_state()
        for l in self._instr:
            parts = l.split(" ")
            n = int(parts[1])
            f = int(parts[3])-1
            t = int(parts[5])-1
            for i in range(n):
                stacks[t].append(stacks[f].pop())
        return "".join(s.pop() for s in stacks)

    def solve_2(self):
        stacks = self._create_init_state()
        for l in self._instr:
            parts = l.split(" ")
            n = int(parts[1])
            f = int(parts[3])-1
            t = int(parts[5])-1
            stacks[t].extend(stacks[f][-n:])
            stacks[f] = stacks[f][:-n]
        return "".join(s.pop() for s in stacks)