import re

import numpy as np

from utils import Solver, get_data


class Solver2018Day3(Solver):
    YEAR = 2018
    DAY = 3

    def __init__(self, src):
        pat = re.compile(r"#(\d+) @ (\d+),(\d+): (\d+)x(\d+)")
        self.ops = [list(map(int, v)) for v in pat.findall(src.strip())]
        self.ans1 = self.ans2 = None

    def run(self):
        n = 1002
        s = np.zeros((n, n), dtype=int)
        for _, x, y, dx, dy in self.ops:
            s[x:x + dx, y:y + dy] += 1
        self.ans1 = (s > 1).sum()
        for id, x, y, dx, dy in self.ops:
            if np.all(s[x:x + dx, y:y + dy] == 1):
                self.ans2 = id

    def solve_part_1(self):
        return self.ans1

    def solve_part_2(self):
        return self.ans2


if __name__ == "__main__":
    src = get_data(Solver2018Day3.YEAR, Solver2018Day3.DAY)
    sol = Solver2018Day3(src)
    sol.run()
    print(sol.solve_part_1())
    print(sol.solve_part_2())
