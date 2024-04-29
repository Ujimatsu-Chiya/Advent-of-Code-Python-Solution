import re
from collections import Counter

import numpy as np
import requests

from utils import Solver


class Solver18D3(Solver):
    INPUT_URL = 'https://adventofcode.com/2018/day/3/input'

    def parse(self, src):
        pat = re.compile(r"#(\d+) @ (\d+),(\d+): (\d+)x(\d+)")
        return [list(map(int, v)) for v in pat.findall(src.strip())]

    def _solve(self, ls):
        n = 1002
        s = np.zeros((n, n), dtype=int)
        for _, x, y, dx, dy in ls:
            s[x:x + dx, y:y + dy] += 1
        return s

    def solve_part_1(self, src):
        ls = self.parse(src)
        s = self._solve(ls)
        return (s > 1).sum()

    def solve_part_2(self, src):
        ls = self.parse(src)
        s = self._solve(ls)
        for id, x, y, dx, dy in ls:
            if np.all(s[x:x + dx, y:y + dy] == 1):
                return id


if __name__ == "__main__":
    sol = Solver18D3()
    session = open('../.session').read().strip()
    cookies = {'session': session}

    src = requests.get(Solver18D3.INPUT_URL, cookies=cookies).text
    print(sol.solve_part_1(src))
    print(sol.solve_part_2(src))
