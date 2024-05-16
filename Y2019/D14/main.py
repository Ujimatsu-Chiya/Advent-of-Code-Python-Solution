import re

from utils import Solver, get_data
from collections import deque, defaultdict


class Solver2019Day14(Solver):
    YEAR = 2019
    DAY = 14

    def __init__(self, src):
        ls = src.strip().split('\n')
        pat = re.compile(r"(\d+)\s+([A-Z]+)")
        self.mp = {}
        for s in ls:
            tmp = [[int(x), t] for x, t in pat.findall(s)]
            l, r = tmp[:-1], tmp[-1]
            self.mp[r[1]] = [r[0], l]

    def _run(self, need):
        q = deque()
        deg = defaultdict(int)
        f = defaultdict(int)
        for k in self.mp.keys():
            deg[k] = 0
        for _, vec in self.mp.values():
            for _, u in vec:
                deg[u] += 1
        st, ed = "FUEL", "ORE"
        f[st] = need
        q.append(st)
        while len(q):
            u = q.popleft()
            if u in self.mp.keys():
                per, vec = self.mp[u]
                block = (f[u] + per - 1) // per
                for cnt, v in vec:
                    f[v] += block * cnt
                    deg[v] -= 1
                    if deg[v] == 0:
                        q.append(v)
        return f[ed]

    def solve_part_1(self):
        return self._run(1)

    def solve_part_2(self):
        M = 10 ** 12
        l, r = 0, M
        while l < r:
            mid = (l + r + 1) >> 1
            if self._run(mid) <= M:
                l = mid
            else:
                r = mid - 1
        return l


if __name__ == "__main__":
    src = get_data(Solver2019Day14.YEAR, Solver2019Day14.DAY)
    sol = Solver2019Day14(src)
    print(sol.solve_part_1())
    print(sol.solve_part_2())
