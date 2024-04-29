import re
from itertools import count

import requests

from utils import Solver


class Solver16D15(Solver):
    INPUT_URL = 'https://adventofcode.com/2016/day/15/input'

    def parse(self, src):
        pat = re.compile(r"Disc #(\d+) has (\d+) positions; at time=(\d+), it is at position (\d+).")
        ls = []
        for tp in pat.findall(src.strip()):
            ls.append([int(tp[1]), int(tp[3])])
        return ls

    def _solve(self, ls):
        for tm in count():
            if all((tm + i + 1 + t[1]) % t[0] == 0 for i, t in enumerate(ls)):
                return tm

    def solve_part_1(self, src):
        ls = self.parse(src)
        return self._solve(ls)

    def solve_part_2(self, src):
        ls = self.parse(src) + [[11, 0]]
        return self._solve(ls)


if __name__ == "__main__":
    sol = Solver16D15()
    session = open('../.session').read().strip()
    cookies = {'session': session}
    src = requests.get(Solver16D15.INPUT_URL, cookies=cookies).text
    print(sol.solve_part_1(src))
    print(sol.solve_part_2(src))
