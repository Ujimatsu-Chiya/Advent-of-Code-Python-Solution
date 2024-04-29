from itertools import count

import requests

from utils import Solver


class Solver18D14(Solver):
    INPUT_URL = 'https://adventofcode.com/2018/day/14/input'

    def parse(self, src):
        return int(src.strip())

    def solve_part_1(self, src):
        n = self.parse(src)
        a = [3, 7]
        p0 = 0
        p1 = 1
        while len(a) < n + 10:
            x = a[p0] + a[p1]
            if x >= 10:
                a.append(1)
                x -= 10
            a.append(x)
            p0 = (p0 + 1 + a[p0]) % len(a)
            p1 = (p1 + 1 + a[p1]) % len(a)
        return "".join(str(x) for x in a[n:n + 10])

    def solve_part_2(self, src):
        n = self.parse(src)
        b = [int(x) for x in str(n)]
        a = [3, 7]
        p0 = 0
        p1 = 1
        for p in count():
            while len(a) < p + len(b):
                x = a[p0] + a[p1]
                if x >= 10:
                    a.append(1)
                    x -= 10
                a.append(x)
                p0 = (p0 + 1 + a[p0]) % len(a)
                p1 = (p1 + 1 + a[p1]) % len(a)
            if a[p:p + len(b)] == b:
                return p


if __name__ == "__main__":
    sol = Solver18D14()
    session = open('../.session').read().strip()
    cookies = {'session': session}

    src = requests.get(Solver18D14.INPUT_URL, cookies=cookies).text
    print(sol.solve_part_1(src))
    print(sol.solve_part_2(src))
