import re
from collections import Counter, defaultdict

import numpy as np
import requests

from utils import Solver


class Solver18D6(Solver):
    INPUT_URL = 'https://adventofcode.com/2018/day/6/input'

    def parse(self, src):
        pat = re.compile(r"(\d+)\s*,\s*(\d+)")
        return [list(map(int, v)) for v in pat.findall(src.strip())]

    def solve_part_1(self, src):
        ls = self.parse(src)
        n = len(ls)
        mnx = min(v[0] for v in ls)
        mxx = max(v[0] for v in ls)
        mny = min(v[1] for v in ls)
        mxy = max(v[1] for v in ls)
        inf = mxx - mnx + mxy - mny
        mp = defaultdict(int)
        border = set()
        for i in range(mnx, mxx + 1):
            for j in range(mny, mxy + 1):
                mn, pt = inf, -1
                for k in range(n):
                    d = abs(ls[k][0] - i) + abs(ls[k][1] - j)
                    if d < mn:
                        mn, pt = d, k
                    elif d == mn:
                        pt = None
                if pt is not None:
                    mp[pt] += 1
                    if i in [mnx, mxx] or j in [mny, mxy]:
                        border.add(pt)
        for x in border:
            mp.pop(x)
        return max(mp.values())

    def solve_part_2(self, src):
        ls = self.parse(src)
        n = len(ls)
        mnx = min(v[0] for v in ls)
        mxx = max(v[0] for v in ls)
        mny = min(v[1] for v in ls)
        mxy = max(v[1] for v in ls)
        M = 10000
        ans = 0
        for i in range(mnx, mxx + 1):
            for j in range(mny, mxy + 1):
                d = 0
                for k in range(n):
                    d += abs(ls[k][0] - i) + abs(ls[k][1] - j)
                if d < M:
                    ans += 1
        return ans



if __name__ == "__main__":
    sol = Solver18D6()
    session = open('../.session').read().strip()
    cookies = {'session': session}

    src = requests.get(Solver18D6.INPUT_URL, cookies=cookies).text
    print(sol.solve_part_1(src))
    print(sol.solve_part_2(src))
