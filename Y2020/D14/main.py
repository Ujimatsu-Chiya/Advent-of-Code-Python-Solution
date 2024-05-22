import re
from collections import defaultdict

from utils import Solver, get_data


class Solver2020Day14(Solver):
    YEAR = 2020
    DAY = 14

    def __init__(self, src):
        pat = re.compile(r'mask\s*=\s*([X01]+)|mem\[(\d+)\]\s*=\s*(\d+)')
        self.ops = []
        for match in pat.findall(src.strip()):
            if match[0]:
                self.ops.append(["mask", match[0]])
            else:
                self.ops.append(["mem", int(match[1]), int(match[2])])

    def solve_part_1(self):
        mask_or, mask_and = -1, -1
        mp = defaultdict(int)
        for v in self.ops:
            op = v[0]
            if op == "mask":
                mask_or, mask_and = int(v[1].replace('X', '0'), 2), int(v[1].replace('X', '1'), 2)
            else:
                x, y = v[1], v[2]
                mp[x] = y & mask_and | mask_or
        return sum(mp.values())

    def solve_part_2(self):
        M = 36
        mask, fix = -1, -1
        mp = defaultdict(int)
        for v in self.ops:
            op = v[0]
            if op == "mask":
                mask = int(v[1].replace('1', '0').replace('X', '1'), 2)
                fix = int(v[1].replace('X', '0'), 2)
            else:
                x, y = (v[1] | fix) & (((1 << M) - 1) ^ mask), v[2]
                j = mask
                while True:
                    mp[x | j] = y
                    if j == 0:
                        break
                    j = (j - 1) & mask
        return sum(mp.values())


if __name__ == "__main__":
    src = get_data(Solver2020Day14.YEAR, Solver2020Day14.DAY)
    sol = Solver2020Day14(src)
    print(sol.solve_part_1())
    print(sol.solve_part_2())
