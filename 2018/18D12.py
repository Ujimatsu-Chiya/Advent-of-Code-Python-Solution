import re
from itertools import count

import numpy as np
import requests

from utils import Solver


class Solver18D12(Solver):
    INPUT_URL = 'https://adventofcode.com/2018/day/12/input'

    def parse(self, src):
        pat = re.compile(r'([.#]{5}) => ([.#])')
        mp = {}
        for l, r in pat.findall(src.strip()):
            tp = tuple(i - 2 for i in range(len(l)) if l[i] == '#')
            mp[tp] = (r == '#')
        s = re.search(r'initial state: ([.#]+)', src.strip()).group(1)
        return set(i for i in range(len(s)) if s[i] == '#'), mp

    def solve_part_1(self, src):
        s, mp = self.parse(src)
        N = 20
        for _ in range(N):
            l, r = min(s), max(s)
            t = set()
            for i in range(l - 2, r + 2 + 1):
                tp = tuple(d for d in range(-2, 3) if i + d in s)
                if mp[tp]:
                    t.add(i)
            s = t
        return sum(s)

    def solve_part_2(self, src):
        s, mp = self.parse(src)
        M = 50000000000
        state_ls = []
        st = T = d = -1
        for i in count():
            a = sorted(s)
            tp = tuple(a[i + 1] - a[i] for i in range(len(a) - 1))
            if tp in mp.keys():
                T = i - mp[tp][0]
                st = mp[tp][0]
                d = a[0] - mp[tp][1][0]
                break
            mp[tp] = i, a
            state_ls.append(a)
            l, r = min(s), max(s)
            t = set()
            for i in range(l - 2, r + 2 + 1):
                tp = tuple(d for d in range(-2, 3) if i + d in s)
                if mp[tp]:
                    t.add(i)
            s = t
        if st >= M:
            pos = state_ls[M]
        else:
            q, m = divmod(M - st, T)
            idx = st + m
            pos = [q * d + state_ls[idx][i] for i in range(len(state_ls[idx]))]
        return sum(pos)


if __name__ == "__main__":
    sol = Solver18D12()
    session = open('../.session').read().strip()
    cookies = {'session': session}

    src = requests.get(Solver18D12.INPUT_URL, cookies=cookies).text
    print(sol.solve_part_1(src))
    print(sol.solve_part_2(src))
