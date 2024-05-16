import re

from utils import Solver, get_data
from math import lcm
from itertools import count


class Solver2019Day12(Solver):
    YEAR = 2019
    DAY = 12

    def __init__(self, src):
        pat = re.compile(r"<x=(-?\d+),\s*y=(-?\d+),\s*z=(-?\d+)>")
        self.ls = []
        for u in pat.findall(src.strip()):
            self.ls.append(list(map(int, u)))

    def solve_part_1(self):
        def solve(a, M):
            v = [0 for _ in range(len(a))]
            for _ in range(M):
                b = []
                for i, x in enumerate(a):
                    v[i] += sum(1 if w > x else -1 if w < x else 0 for w in a)
                    b.append(a[i] + v[i])
                a = b
            return a, v

        M = 1000
        d_list, v_list = [], []
        for a in zip(*self.ls):
            d, v = solve(a, M)
            d_list.append(d)
            v_list.append(v)
        ans = 0
        for d, v in zip(zip(*d_list), zip(*v_list)):
            ans += sum(abs(x) for x in d) * sum(abs(x) for x in v)
        return ans

    def solve_part_2(self):
        def solve(a):
            v = [0 for _ in range(len(a))]
            a0, v0 = tuple(a), tuple(v)
            for i in count():
                b = []
                for j, x in enumerate(a):
                    v[j] += sum(1 if w > x else -1 if w < x else 0 for w in a)
                    b.append(a[j] + v[j])
                a = tuple(b)
                if a == a0 and tuple(v) == v0:
                    return i + 1

        t = [solve(tuple(a)) for a in zip(*self.ls)]
        return lcm(*t)


if __name__ == "__main__":
    src = get_data(Solver2019Day12.YEAR, Solver2019Day12.DAY)
    sol = Solver2019Day12(src)
    print(sol.solve_part_1())
    print(sol.solve_part_2())
