import re

import requests

from utils import Solver


class Solver17D15(Solver):
    INPUT_URL = 'https://adventofcode.com/2017/day/15/input'

    def parse(self, src):
        a = re.findall(r'\d+', src.strip())
        return list(map(int, a))

    def solve_part_1(self, src):
        a, b = self.parse(src)
        ma, mb = 16807, 48271
        mod = (1 << 31) - 1
        msk = (1 << 16) - 1
        M = 40000000
        ans = 0
        for i in range(M):
            a = a * ma % mod
            b = b * mb % mod
            if ((a - b) & msk) == 0:
                ans += 1
        return ans

    def solve_part_2(self, src):
        a, b = self.parse(src)
        ma, mb = 16807, 48271
        mod = (1 << 31) - 1
        msk = (1 << 16) - 1

        def gen(st, m, bit):
            x = st
            msk_now = (1 << bit) - 1
            while True:
                x = x * m % mod
                if (x & msk_now) == 0:
                    yield x

        A = gen(a, ma, 2)
        B = gen(b, mb, 3)
        M = 5000000
        ans = 0
        for i in range(M):
            a = next(A)
            b = next(B)
            if ((a - b) & msk) == 0:
                ans += 1
        return ans



if __name__ == "__main__":
    sol = Solver17D15()
    session = open('../.session').read().strip()
    cookies = {'session': session}

    src = requests.get(Solver17D15.INPUT_URL, cookies=cookies).text
    print(sol.solve_part_1(src))
    print(sol.solve_part_2(src))
