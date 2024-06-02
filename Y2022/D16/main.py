import re
from collections import deque, defaultdict

from utils import Solver, get_data


class Solver2022Day16(Solver):
    YEAR = 2022
    DAY = 16

    def __init__(self, src):
        pat = re.compile(r"Valve (\w+) has flow rate=(\d+); tunnel[s]? lead[s]? to valves? ([\w, ]+)")
        self.pressure = {}
        self.mp = {}
        for name, v, s in pat.findall(src.strip()):
            self.pressure[name] = int(v)
            self.mp[name] = s.split(', ')
        self.ans1 = self.ans2 = None

    def run(self):
        keys = [k for k, v in self.pressure.items() if v > 0]
        pressure = [self.pressure[k] for i, k in enumerate(keys)]
        M1 = 30
        M2 = 26
        f = [defaultdict(int) for _ in range(M1 + 1)]
        n = len(keys)
        g = [[-1 for _ in range(n)] for _ in range(n)]
        start = [-1 for _ in range(n)]
        for i, st in enumerate(keys + ['AA']):
            d = {st: 0}
            q = deque([st])
            while len(q) > 0:
                u = q.popleft()
                for v in self.mp[u]:
                    if v not in d.keys():
                        d[v] = d[u] + 1
                        q.append(v)
            for j, ed in enumerate(keys):
                if st == 'AA':
                    start[j] = d[ed] + 1
                else:
                    g[i][j] = d[ed] + 1
        for j, tm in enumerate(start):
            f[tm][1 << j, j] = 0
        record = defaultdict(int)
        self.ans1 = self.ans2 = 0
        for tm, mp in enumerate(f):
            for (st, u), val in mp.items():
                s = 0
                for i in range(n):
                    if st >> i & 1:
                        s += pressure[i]
                self.ans1 = max(self.ans1, val + s * (M1 - tm))
                if tm <= M2:
                    record[st] = max(record[st], val + s * (M2 - tm))
                for v in range(n):
                    if (st >> v & 1) == 0 and tm + g[u][v] <= M1:
                        f[tm + g[u][v]][st | 1 << v, v] = max(f[tm + g[u][v]][st | 1 << v, v], val + g[u][v] * s)
        record = sorted(record.items(), key=lambda v: v[1], reverse=True)
        for i, (s1, v1) in enumerate(record):
            if v1 * 2 < self.ans2:
                break
            for s2, v2 in record[i+1:]:
                if not (s1 & s2):
                    self.ans2 = max(self.ans2, v1 + v2)
                if v1 + v2 < self.ans2:
                    break

    def solve_part_1(self):
        return self.ans1

    def solve_part_2(self):
        return self.ans2


if __name__ == "__main__":
    src = get_data(Solver2022Day16.YEAR, Solver2022Day16.DAY)
    sol = Solver2022Day16(src)
    sol.run()
    print(sol.solve_part_1())
    print(sol.solve_part_2())
