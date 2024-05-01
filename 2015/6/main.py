import re

from utils import Solver, get_data


class Solver2015Day6(Solver):
    YEAR = 2015
    DAY = 6

    def parse(self, src):
        ls = re.findall("(toggle|turn on|turn off)\s(\d*),(\d*)\sthrough\s(\d*),(\d*)", src)
        return [[int(s) if s.isdigit() else s for s in v] for v in ls]

    def solve_part_1(self, src):
        M = 1000
        f = [[0 for _ in range(M)] for _ in range(M)]
        ls = self.parse(src)
        for order, xa, ya, xb, yb in ls:
            for i in range(xa, xb + 1):
                for j in range(ya, yb + 1):
                    if order == "toggle":
                        f[i][j] ^= 1
                    elif order == "turn on":
                        f[i][j] = 1
                    else:
                        f[i][j] = 0
        return sum(sum(v) for v in f)

    def solve_part_2(self, src):
        M = 1000
        f = [[0 for _ in range(M)] for _ in range(M)]
        ls = self.parse(src)
        for order, xa, ya, xb, yb in ls:
            for i in range(xa, xb + 1):
                for j in range(ya, yb + 1):
                    if order == "toggle":
                        f[i][j] += 2
                    elif order == "turn on":
                        f[i][j] += 1
                    else:
                        f[i][j] = max(f[i][j] - 1, 0)
        return sum(sum(v) for v in f)


if __name__ == "__main__":
    sol = Solver2015Day6()
    src = get_data(Solver2015Day6.YEAR, Solver2015Day6.DAY)
    print(sol.solve_part_1(src))
    print(sol.solve_part_2(src))
