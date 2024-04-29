import re

import requests

from utils import Solver


class Solver15D25(Solver):
    INPUT_URL = 'https://adventofcode.com/2015/day/25/input'

    def parse(self, src):
        a = re.findall(r'\d+', src.strip())
        return list(int(x) for x in a)

    def solve_part_1(self, src):
        r, c = self.parse(src)
        t = r - 1 + c - 1
        x = (t + 1) * t // 2 + c - 1
        s0 = 20151125
        k = 252533
        mod = 33554393
        return s0 * pow(k, x, mod) % mod

    def solve_part_2(self, src):
        pass


if __name__ == "__main__":
    sol = Solver15D25()
    session = open('../.session').read().strip()
    cookies = {'session': session}
    src = requests.get(Solver15D25.INPUT_URL, cookies=cookies).text
    print(sol.solve_part_1(src))
    print(sol.solve_part_2(src))
