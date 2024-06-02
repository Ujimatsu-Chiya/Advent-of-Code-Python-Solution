import re
from itertools import pairwise, count

from utils import Solver, get_data
from collections import defaultdict


class Solver2022Day14(Solver):
    YEAR = 2022
    DAY = 14

    def __init__(self, src):
        self.mp = defaultdict(int)
        pat = re.compile(r'(\d+),(\d+)')
        for s in src.strip().split('\n'):
            ls = []
            for x, y in pat.findall(s):
                ls.append([int(x), int(y)])
            for p0, p1 in pairwise(ls):
                for i in range(min(p0[0], p1[0]), max(p0[0], p1[0]) + 1):
                    for j in range(min(p0[1], p1[1]), max(p0[1], p1[1]) + 1):
                        self.mp[i, j] = 1
        self.ans1 = self.ans2 = None

    def run(self):
        X, Y = 500, 0
        mxy = max(v[1] for v in self.mp.keys())
        mnx = min(v[0] for v in self.mp.keys())
        mxx = max(v[0] for v in self.mp.keys())
        for i in count():
            x, y = X, Y
            if self.mp[X, Y] != 0:
                self.ans2 = i
                break
            while True:
                if y + 1 == mxy + 2:
                    break
                elif self.mp[x, y + 1] == 0:
                    pass
                elif self.mp[x - 1, y + 1] == 0:
                    x -= 1
                elif self.mp[x + 1, y + 1] == 0:
                    x += 1
                else:
                    break
                y += 1
                if y > mxy and self.ans1 is None:
                    self.ans1 = i
            self.mp[x, y] = 2


    def solve_part_1(self):
        return self.ans1

    def solve_part_2(self):
        return self.ans2


if __name__ == "__main__":
    src = get_data(Solver2022Day14.YEAR, Solver2022Day14.DAY)
    sol = Solver2022Day14(src)
    sol.run()
    print(sol.solve_part_1())
    print(sol.solve_part_2())
