import re

import numpy as np

from utils import Solver, get_data


class Solver2018Day3(Solver):
    YEAR = 2018
    DAY = 3

    def parse(self, src):
        pat = re.compile(r"#(\d+) @ (\d+),(\d+): (\d+)x(\d+)")
        return [list(map(int, v)) for v in pat.findall(src.strip())]

    def _solve(self, ls):
        n = 1002
        s = np.zeros((n, n), dtype=int)
        for _, x, y, dx, dy in ls:
            s[x:x + dx, y:y + dy] += 1
        return s

    def solve_part_1(self, src):
        ls = self.parse(src)
        s = self._solve(ls)
        return (s > 1).sum()

    def solve_part_2(self, src):
        ls = self.parse(src)
        s = self._solve(ls)
        for id, x, y, dx, dy in ls:
            if np.all(s[x:x + dx, y:y + dy] == 1):
                return id


if __name__ == "__main__":
    sol = Solver2018Day3()
    src = get_data(Solver2018Day3.YEAR, Solver2018Day3.DAY)
    print(sol.solve_part_1(src))
    print(sol.solve_part_2(src))
