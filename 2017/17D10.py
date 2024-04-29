import operator
from functools import reduce

import requests

from utils import Solver


class Solver17D10(Solver):
    INPUT_URL = 'https://adventofcode.com/2017/day/10/input'

    def parse(self, src):
        return src.strip()

    def _solve(self, a):
        M = 256
        b = list(range(M))
        p = 0
        for skip_size, x in enumerate(a):
            if p + x <= M:
                l, m, r = b[:p], b[p:p + x], b[p + x:]
                b = l + list(reversed(m)) + r
            else:
                rev = list(reversed(b[p:] + b[:x - (M - p)]))
                rest = b[x - (M - p):p]
                b = rev[- (x - (M - p)):] + rest + rev[:-(x - (M - p))]
            p = (p + x + skip_size) % M
            skip_size += 1
        return b

    def solve_part_1(self, src):
        a = list(map(int, self.parse(src).split(',')))
        b = self._solve(a)
        return b[0] * b[1]

    def solve_part_2(self, src):
        s = self.parse(src)
        a = [ord(x) for x in s]
        a = (a + [17, 31, 73, 47, 23]) * 64
        b = self._solve(a)
        t = [reduce(operator.xor, b[i:i + 16]) for i in range(0, len(b), 16)]
        return "".join("{:02x}".format(x) for x in t)


if __name__ == "__main__":
    sol = Solver17D10()
    session = open('../.session').read().strip()
    cookies = {'session': session}

    src = requests.get(Solver17D10.INPUT_URL, cookies=cookies).text
    print(sol.solve_part_1(src))
    print(sol.solve_part_2(src))
