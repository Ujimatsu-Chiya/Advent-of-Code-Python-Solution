import re
from collections import Counter

import requests

from utils import Solver


class Solver18D2(Solver):
    INPUT_URL = 'https://adventofcode.com/2018/day/2/input'

    def parse(self, src):
        return src.strip().split()

    def solve_part_1(self, src):
        ls = self.parse(src)
        c2 = c3 = 0
        for s in ls:
            v = Counter(s).values()
            if 2 in v:
                c2 += 1
            if 3 in v:
                c3 += 1
        return c2 * c3

    def solve_part_2(self, src):
        ls = self.parse(src)
        a = []
        for i in range(len(ls)):
            for j in range(i):
                a.append([len([1 for k in range(len(ls[j])) if ls[i][k] != ls[j][k]]), i, j])
        a.sort()
        x, y = a[0][1:]
        return "".join(ls[x][i] for i in range(len(ls[x])) if ls[x][i] == ls[y][i])


if __name__ == "__main__":
    sol = Solver18D2()
    session = open('../.session').read().strip()
    cookies = {'session': session}

    src = requests.get(Solver18D2.INPUT_URL, cookies=cookies).text
    print(sol.solve_part_1(src))
    print(sol.solve_part_2(src))
