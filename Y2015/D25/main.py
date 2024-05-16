import re

from utils import Solver, get_data


class Solver2015Day25(Solver):
    YEAR = 2015
    DAY = 25

    def __init__(self, src):
        a = re.findall(r'\d+', src.strip())
        self.r, self.c = list(int(x) for x in a)

    def solve_part_1(self):
        r, c = self.r, self.c
        t = r - 1 + c - 1
        x = (t + 1) * t // 2 + c - 1
        s0 = 20151125
        k = 252533
        mod = 33554393
        return s0 * pow(k, x, mod) % mod

    def solve_part_2(self):
        pass


if __name__ == "__main__":
    src = get_data(Solver2015Day25.YEAR, Solver2015Day25.DAY)
    sol = Solver2015Day25(src)
    print(sol.solve_part_1())
    print(sol.solve_part_2())
