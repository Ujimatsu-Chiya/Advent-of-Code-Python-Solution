import re
from collections import defaultdict

from utils import Solver, get_data


class Solver2017Day24(Solver):
    YEAR = 2017
    DAY = 24

    def __init__(self, src):
        pat = re.compile(r"(\d+)/(\d+)")
        self.ls = [list(map(int, v)) for v in pat.findall(src.strip())]
        self.ans1 = self.ans2 = None

    def run(self):
        mp = defaultdict(list)
        for i, t in enumerate(self.ls):
            mp[t[0]].append((t[1], i))
            mp[t[1]].append((t[0], i))
        vis = [False for _ in range(len(self.ls))]
        ans = []

        def dfs(u, s, l):
            ok = True
            for v, id in mp[u]:
                if not vis[id]:
                    ok = False
                    vis[id] = True
                    dfs(v, s + u + v, l + 1)
                    vis[id] = False
            if ok:
                ans.append((s, l))

        dfs(0, 0, 0)
        self.ans1 = max(v[0] for v in ans)
        mx = max(v[1] for v in ans)
        self.ans2 = max(v[0] for v in ans if mx == v[1])

    def solve_part_1(self):
        return self.ans1

    def solve_part_2(self):
        return self.ans2


if __name__ == "__main__":
    src = get_data(Solver2017Day24.YEAR, Solver2017Day24.DAY)
    sol = Solver2017Day24(src)
    sol.run()
    print(sol.solve_part_1())
    print(sol.solve_part_2())
