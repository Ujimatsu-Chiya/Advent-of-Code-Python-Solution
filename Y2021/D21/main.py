import re
from collections import Counter
from functools import lru_cache
from itertools import cycle, count, product

from utils import Solver, get_data


class Solver2021Day21(Solver):
    YEAR = 2021
    DAY = 21

    def __init__(self, src):
        pat = re.compile(r"(\d+)")
        ls = pat.findall(src.strip())
        self.pos = int(ls[1]) - 1, int(ls[2]) - 1

    def solve_part_1(self):
        N = 10
        M = 100
        W = 1000
        gen = cycle(range(1, M + 1, 1))
        vals = [0, 0]
        pos = list(self.pos)
        for r in count(0):
            id = r & 1
            pos[id] = (pos[id] + next(gen) + next(gen) + next(gen)) % N
            vals[id] += pos[id] + 1
            if vals[id] >= W:
                return vals[id ^ 1] * (r + 1) * 3

    def solve_part_2(self):
        N = 10
        W = 21
        M = 3
        c = Counter(sum(v) for v in product(range(1, M + 1), repeat=3))

        @lru_cache(maxsize=None)
        def dfs(vals, pos, p):
            if vals[0] >= W:
                return 1, 0
            elif vals[1] >= W:
                return 0, 1
            c0 = c1 = 0
            for d, cnt in c.items():
                new_pos = (pos[p] + d) % N
                new_val = vals[p] + new_pos + 1
                w0, w1 = dfs((vals[0], new_val) if p == 1 else (new_val, vals[1]),
                             (pos[0], new_pos) if p == 1 else (new_pos, pos[1]),
                             p ^ 1)
                c0 += w0 * cnt
                c1 += w1 * cnt
            return c0, c1

        return max(dfs((0, 0), self.pos, 0))


if __name__ == "__main__":
    src = get_data(Solver2021Day21.YEAR, Solver2021Day21.DAY)
    sol = Solver2021Day21(src)
    print(sol.solve_part_1())
    print(sol.solve_part_2())