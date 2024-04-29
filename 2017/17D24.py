import re
from collections import defaultdict

import requests

from utils import Solver


class Solver17D24(Solver):
    INPUT_URL = 'https://adventofcode.com/2017/day/24/input'

    def parse(self, src):
        pat = re.compile(r"(\d+)/(\d+)")
        return [list(map(int, v)) for v in pat.findall(src.strip())]

    def solve_part_1(self, src):
        ls = self.parse(src)
        mp = defaultdict(list)
        for i, t in enumerate(ls):
            mp[t[0]].append((t[1], i))
            mp[t[1]].append((t[0], i))
        vis = [False for _ in range(len(ls))]
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
        return max(v[0] for v in ans)

    def solve_part_2(self, src):
        ls = self.parse(src)
        mp = defaultdict(list)
        for i, t in enumerate(ls):
            mp[t[0]].append((t[1], i))
            mp[t[1]].append((t[0], i))
        vis = [False for _ in range(len(ls))]
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
        mx = max(v[1] for v in ans)
        return max(v[0] for v in ans if mx == v[1])


if __name__ == "__main__":
    sol = Solver17D24()
    session = open('../.session').read().strip()
    cookies = {'session': session}

    src = requests.get(Solver17D24.INPUT_URL, cookies=cookies).text
    print(sol.solve_part_1(src))
    print(sol.solve_part_2(src))
