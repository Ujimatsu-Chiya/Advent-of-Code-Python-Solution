import re
from collections import defaultdict

from utils import Solver, get_data


class Solver2018Day6(Solver):
    YEAR = 2018
    DAY = 6

    def __init__(self, src):
        pat = re.compile(r"(\d+)\s*,\s*(\d+)")
        self.ls = [list(map(int, v)) for v in pat.findall(src.strip())]
        self.ans1 = self.ans2 = None

    def run(self):
        ls = self.ls
        self.ans2 = 0
        M = 10000
        n = len(ls)
        mnx = min(v[0] for v in ls)
        mxx = max(v[0] for v in ls)
        mny = min(v[1] for v in ls)
        mxy = max(v[1] for v in ls)
        mp = defaultdict(int)
        border = set()
        for i in range(mnx, mxx + 1):
            for j in range(mny, mxy + 1):
                d_list = [abs(ls[k][0] - i) + abs(ls[k][1] - j) for k in range(n)]
                mn = min(d_list)
                k_list = [k for k in range(n) if d_list[k] == mn]
                if len(k_list) == 1:
                    mp[k_list[0]] += 1
                    if i in [mnx, mxx] or j in [mny, mxy]:
                        border.add(k_list[0])
                if sum(d_list) < M:
                    self.ans2 += 1
        for x in border:
            mp.pop(x)
        self.ans1 = max(mp.values())

    def solve_part_1(self):
        return self.ans1

    def solve_part_2(self):
        return self.ans2


if __name__ == "__main__":
    src = get_data(Solver2018Day6.YEAR, Solver2018Day6.DAY)
    sol = Solver2018Day6(src)
    sol.run()
    print(sol.solve_part_1())
    print(sol.solve_part_2())
