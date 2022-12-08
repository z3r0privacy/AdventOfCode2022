from aoc2022.day import Day

class Day07 (Day):
    class FSEntry:
        def __init__(self, name, parent, size) -> None:
            self.name = name
            self.parent = parent
            self.entries = []
            if size is None:
                self.is_dir = True
            else:
                self.size = size
                self.is_dir = False
        
        def get_size(self):
            if self.is_dir:
                return sum(e.get_size() for e in self.entries)
            return self.size

        def get_subdir(self, name):
            if name not in [e.name for e in self.entries if e.is_dir]:
                d = Day07.FSEntry(name, self, None)
                self.entries.append(d)
            return [e for e in self.entries if e.name == name][0]

        def add_file(self, name, size):
            f = Day07.FSEntry(name, self, size)
            self.entries.append(f)

        def add_to_list_if_ret_size(self, pred, l):
            size = 0
            if self.is_dir:
                size = sum(e.add_to_list_if_ret_size(pred, l) for e in self.entries)
            else:
                size = self.size
            if pred(self, size):
                l.append(size)
            return size


    def __init__(self):
        super().__init__(__name__)
        self._isdone = True
        self._stdinout = self.read_file_lines()
        self._root_dir = Day07.FSEntry("/", None, None)

    def _parse_ls(self, line_nr, curr_dir):
        line_count = 0
        line_nr += 1
        while line_nr < len(self._stdinout) and self._stdinout[line_nr][0] != "$":
            line_count += 1
            l = self._stdinout[line_nr]
            if l.startswith("dir"):
                curr_dir.get_subdir(l[4:])
            else:
                size, name = l.split(" ")
                size = int(size)
                curr_dir.add_file(name, size)
            line_nr += 1
        return line_count

    def solve_1(self):
        curr_dir = None
        i = 0
        while i < len(self._stdinout):
            io = self._stdinout[i]
            if io[0] == "$":
                if io == "$ cd /":
                    curr_dir = self._root_dir
                elif io == "$ cd ..":
                    curr_dir = curr_dir.parent
                elif io.startswith("$ cd"):
                    curr_dir = curr_dir.get_subdir(io[5:])
                elif io == "$ ls":
                    num_entries = self._parse_ls(i, curr_dir)
                    i += num_entries
            i += 1
        small_dirs = []
        pred = lambda e,s: e.is_dir and s <= 100000
        self._root_dir.add_to_list_if_ret_size(pred, small_dirs)
        return sum(small_dirs)


    def solve_2(self):
        space_to_free = 30000000 - (70000000 - self._root_dir.get_size())
        big_dirs = []
        pred = lambda e,s: e.is_dir and s >= space_to_free
        self._root_dir.add_to_list_if_ret_size(pred, big_dirs)
        return min(big_dirs)