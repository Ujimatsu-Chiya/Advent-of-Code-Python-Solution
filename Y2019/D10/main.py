from utils import Solver, get_data
from math import gcd
from collections import defaultdict
from tools import Point, sgn
from functools import cmp_to_key


class Solver2019Day10(Solver):
    YEAR = 2019
    DAY = 10

    def __init__(self, src):
        mp = src.strip().split()
        self.ls = []
        for i in range(len(mp)):
            for j in range(len(mp[0])):
                if mp[i][j] == '#':
                    self.ls.append(Point(i, j))
        self.ls.sort()
        self.ans1 = self.ans2 = None

    def run(self):
        n = len(self.ls)
        mp_list = [defaultdict(list) for _ in range(n)]
        for j in range(n):
            for i in range(j):
                dp = self.ls[j] - self.ls[i]
                dp = dp // gcd(dp.x, dp.y)
                mp_list[i][dp].append(j)
                mp_list[j][-dp].append(i)

        p = max(range(n), key=lambda k: len(mp_list[k]))
        mp = mp_list[p]
        self.ans1 = len(mp)
        cmp = cmp_to_key(lambda u, v: sgn(v.quadrant() - u.quadrant()) if u.quadrant() != v.quadrant() else sgn(u ^ v))
        a = sorted(mp.keys(), key=cmp)
        pos = a.index(Point(-1, 0))
        a = a[pos:] + a[:pos]
        for k in a:
            mp[k] = sorted(mp[k], key=lambda q: ((self.ls[q] - self.ls[p]).manhattan_dis()), reverse=True)
        M = 200
        order = []
        while len(a) > 0:
            for k in a:
                order.append(mp[k].pop())
            a = [k for k in a if len(mp[k]) > 0]
        p = self.ls[order[M - 1]]
        self.ans2 = p.y * 100 + p.x

    def solve_part_1(self):
        return self.ans1

    def solve_part_2(self):
        return self.ans2


if __name__ == "__main__":
    src = get_data(Solver2019Day10.YEAR, Solver2019Day10.DAY)
    sol = Solver2019Day10(src)
    sol.run()
    print(sol.solve_part_1())
    print(sol.solve_part_2())
