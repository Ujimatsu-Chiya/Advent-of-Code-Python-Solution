import re
from copy import deepcopy
from utils import Solver, get_data


class Solver2022Day5(Solver):
    YEAR = 2022
    DAY = 5

    def __init__(self, src):
        boxes_str, ops_str = src.strip().split('\n\n')
        self.mp = {}
        boxes = boxes_str.split('\n')
        for j in range(len(boxes[-1])):
            if (ch := boxes[-1][j]).isdigit():
                x = int(ch)
                self.mp[x] = []
                for i in range(len(boxes) - 2, -1, -1):
                    ch = boxes[i][j]
                    if ch.isupper():
                        self.mp[x].append(ch)
        pat = re.compile(r'move (\d+) from (\d+) to (\d+)')
        self.ops = [list(map(int, v)) for v in pat.findall(ops_str)]

    def solve_part_1(self):
        mp = deepcopy(self.mp)
        for cnt, v1, v2 in self.ops:
            mp[v2] += mp[v1][-cnt:][::-1]
            mp[v1] = mp[v1][:-cnt]
        return "".join(mp[k][-1] for k in sorted(mp.keys()))

    def solve_part_2(self):
        mp = deepcopy(self.mp)
        for cnt, v1, v2 in self.ops:
            mp[v2] += mp[v1][-cnt:]
            mp[v1] = mp[v1][:-cnt]
        return "".join(mp[k][-1] for k in sorted(mp.keys()))


if __name__ == "__main__":
    src = get_data(Solver2022Day5.YEAR, Solver2022Day5.DAY)
    sol = Solver2022Day5(src)
    print(sol.solve_part_1())
    print(sol.solve_part_2())
