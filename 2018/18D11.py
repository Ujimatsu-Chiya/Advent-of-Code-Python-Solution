import re
from itertools import count

import numpy as np
import requests

from utils import Solver


class Solver18D11(Solver):
    INPUT_URL = 'https://adventofcode.com/2018/day/11/input'

    def parse(self, src):
        return int(src.strip())

    def solve_part_1(self, src):
        n = self.parse(src)
        m = 300
        a = [[0 for _ in range(m + 1)] for _ in range(m + 1)]
        s = [[0 for _ in range(m + 1)] for _ in range(m + 1)]
        for y in range(1, m + 1):
            for x in range(1, m + 1):
                id = x + 10
                a[y][x] = (id * y + n) * id // 100 % 10 - 5
        for i in range(1, m + 1):
            for j in range(1, m + 1):
                s[i][j] = s[i - 1][j] + s[i][j - 1] - s[i - 1][j - 1] + a[i][j]
        mx = -n * n * 9
        for i in range(3, m + 1):
            for j in range(3, m + 1):
                mx = max(mx, s[i][j] - s[i - 3][j] - s[i][j - 3] + s[i - 3][j - 3])
        for i in range(3, m + 1):
            for j in range(3, m + 1):
                if s[i][j] - s[i - 3][j] - s[i][j - 3] + s[i - 3][j - 3] == mx:
                    return "{},{}".format(j - 2, i - 2)

    def solve_part_2(self, src):
        n = self.parse(src)
        m = 300
        a = [[0 for _ in range(m + 1)] for _ in range(m + 1)]
        s = [[0 for _ in range(m + 1)] for _ in range(m + 1)]
        for y in range(1, m + 1):
            for x in range(1, m + 1):
                id = x + 10
                a[y][x] = (id * y + n) * id // 100 % 10 - 5
        for i in range(1, m + 1):
            for j in range(1, m + 1):
                s[i][j] = s[i - 1][j] + s[i][j - 1] - s[i - 1][j - 1] + a[i][j]
        mx = -n * n * 9
        for k in range(1, m + 1):
            for i in range(k, m + 1):
                for j in range(k, m + 1):
                    mx = max(mx, s[i][j] - s[i - k][j] - s[i][j - k] + s[i - k][j - k])
        for k in range(1, m + 1):
            for i in range(k, m + 1):
                for j in range(k, m + 1):
                    if s[i][j] - s[i - k][j] - s[i][j - k] + s[i - k][j - k] == mx:
                        return "{},{},{}".format(j - k + 1, i - k + 1, k)


if __name__ == "__main__":
    sol = Solver18D11()
    session = open('../.session').read().strip()
    cookies = {'session': session}

    src = requests.get(Solver18D11.INPUT_URL, cookies=cookies).text
    print(sol.solve_part_1(src))
    print(sol.solve_part_2(src))
