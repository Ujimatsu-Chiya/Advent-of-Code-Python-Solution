import re
from collections import Counter, defaultdict
from queue import Queue, PriorityQueue

import numpy as np
import requests

from utils import Solver


class Solver18D8(Solver):
    INPUT_URL = 'https://adventofcode.com/2018/day/8/input'

    def parse(self, src):
        return list(map(int, src.strip().split()))

    def solve_part_1(self, src):
        a = self.parse(src)

        def dfs(i):
            ans = 0
            child = a[i]
            meta = a[i + 1]
            p = i + 2
            for _ in range(child):
                ans_t, cnt_t = dfs(p)
                p += cnt_t
                ans += ans_t
            ans += sum(a[p:p + meta])
            p += meta
            return ans, p - i

        return dfs(0)[0]

    def solve_part_2(self, src):
        a = self.parse(src)

        def dfs(i):
            child = a[i]
            meta = a[i + 1]
            ls = []
            p = i + 2
            for _ in range(child):
                val_t, cnt_t = dfs(p)
                p += cnt_t
                ls.append(val_t)
            if child == 0:
                val = sum(a[p:p + meta])
            else:
                val = sum(ls[i-1] for i in a[p:p+meta] if 1 <= i <= len(ls))
            p += meta
            return val, p - i

        return dfs(0)[0]


if __name__ == "__main__":
    sol = Solver18D8()
    session = open('../.session').read().strip()
    cookies = {'session': session}

    src = requests.get(Solver18D8.INPUT_URL, cookies=cookies).text
    print(sol.solve_part_1(src))
    print(sol.solve_part_2(src))
