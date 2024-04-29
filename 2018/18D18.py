from collections import Counter
from itertools import count

import requests

from utils import Solver


class Solver18D18(Solver):
    INPUT_URL = 'https://adventofcode.com/2018/day/18/input'


    def parse(self, src):
        s = src.strip().split()
        t = {'.': 0, '|': 1, '#': 2}
        return tuple(tuple(t[s[i][j]] for j in range(len(s[0]))) for i in range(len(s)))

    def _solve(self, mp, M):
        dirs = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
        n, m = len(mp), len(mp[0])
        mq = {}
        state_ls = []
        st = T = -1
        for i in count():

            if mp in mq.keys():
                T = i - mq[mp]
                st = mq[mp]
                break
            mq[mp] = i
            state_ls.append(mp)
            ls = [[0 for _ in range(m)] for _ in range(n)]
            for i in range(n):
                for j in range(m):
                    c = Counter(mp[i + dx][j + dy] for dx, dy in dirs if 0 <= i + dx < n and 0 <= j + dy < m)
                    if mp[i][j] == 0:
                        ls[i][j] = (1 if c.get(1, 0) >= 3 else 0)
                    elif mp[i][j] == 1:
                        ls[i][j] = (2 if c.get(2, 0) >= 3 else 1)
                    else:
                        ls[i][j] = (2 if c.get(2, 0) >= 1 and c.get(1, 0) >= 1 else 0)
            mp = tuple(tuple(v) for v in ls)

        if st >= M:
            idx = M
        else:
            idx = st + (M - st) % T
        mp = state_ls[idx]
        c1 = sum(v.count(1) for v in mp)
        c2 = sum(v.count(2) for v in mp)
        return c1 * c2

    def solve_part_1(self, src):
        mp = self.parse(src)
        return self._solve(mp, 10)

    def solve_part_2(self, src):
        mp = self.parse(src)
        return self._solve(mp, 1000000000)


if __name__ == "__main__":
    sol = Solver18D18()
    session = open('../.session').read().strip()
    cookies = {'session': session}

    src = requests.get(Solver18D18.INPUT_URL, cookies=cookies).text
    print(sol.solve_part_1(src))
    print(sol.solve_part_2(src))
