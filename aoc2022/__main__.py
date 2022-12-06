import sys, os

# VS Code helper code to find modules
m_dir = sys.path[0]
p_dir = os.path.dirname(m_dir)
sys.path.append(p_dir)
# End VS Code helper code

from aoc2022 import *
from datetime import date, datetime

def print_day(d):
    start = datetime.now()
    s1 = d.solve_1()
    mid = datetime.now()
    s2 = d.solve_2()
    dur2 = datetime.now() - mid
    dur1 = mid - start
    print(f"################## Day {d.Day} ##################")
    print(f"# ({dur1}) Solution 1: {s1}")
    print(f"# ({dur2}) Solution 2: {s2}")
    print("############################################")
    print()

def main():
    days = []
    module = __import__("aoc2022")
    for i in range(1,26):
        name = f"Day{i:02d}"
        try:
            cl = getattr(module, name)
            days.append(cl())
        except AttributeError:
            """Day not (yet) implemented"""

    for d in days:
        if d.Done:
            continue
        print_day(d)

    if any(not d.Done for d in days):
        exit()

    for d in days:
        if not d.Done:
            continue
        print_day(d)

def test():
    return False


if __name__ == "__main__":
    if not test():
        main()