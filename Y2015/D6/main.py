import re
import numpy as np
from utils import Solver, get_data


class Solver2015Day6(Solver):
    YEAR = 2015
    DAY = 6

    def __init__(self, src):
        pat = re.compile(r"(toggle|turn on|turn off)\s(\d*),(\d*)\sthrough\s(\d*),(\d*)")
        ls = pat.findall(src.strip())
        self.ops = [[int(s) if s.isdigit() else s for s in v] for v in ls]

    def solve_part_1(self):
        M = 1000
        f = np.zeros((M, M), dtype=int)
        for order, xa, ya, xb, yb in self.ops:
            if order == "toggle":
                f[xa:xb + 1, ya:yb + 1] ^= 1
            elif order == "turn on":
                f[xa:xb + 1, ya:yb + 1] = 1
            else:
                f[xa:xb + 1, ya:yb + 1] = 0
        return f.sum()

    def solve_part_2(self):
        M = 1000
        f = np.zeros((M, M), dtype=int)
        for order, xa, ya, xb, yb in self.ops:
            if order == "toggle":
                f[xa:xb + 1, ya:yb + 1] += 2
            elif order == "turn on":
                f[xa:xb + 1, ya:yb + 1] += 1
            else:
                tmp = f[xa:xb + 1, ya:yb + 1]
                tmp -= 1
                np.maximum(tmp, 0, out=tmp)
        return sum(sum(v) for v in f)


if __name__ == "__main__":
    src = get_data(Solver2015Day6.YEAR, Solver2015Day6.DAY)
    sol = Solver2015Day6(src)
    print(sol.solve_part_1())
    print(sol.solve_part_2())
