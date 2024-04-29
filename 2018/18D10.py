import re
from collections import defaultdict, deque
from itertools import count

import requests

from utils import Solver


class Solver18D10(Solver):
    INPUT_URL = 'https://adventofcode.com/2018/day/10/input'

    def parse(self, src):
        pat = re.compile(r'position=<\s*(-?\d+),\s*(-?\d+)>\s*velocity=<\s*(-?\d+),\s*(-?\d+)>')
        return [[(int(v[0]), int(v[1])), (int(v[2]), int(v[3]))] for v in pat.findall(src.strip())]

    def _cal_pos(self, pt, tm):
        return tuple((p + v * tm) for p, v in zip(*pt))

    def solve_part_1(self, src):
        ls = self.parse(src)
        n = len(ls)
        for t in count(0):
            lp = [self._cal_pos(pt, t) for pt in ls]
            mnx, mxx = min(v[0] for v in lp), max(v[0] for v in lp)
            mny, mxy = min(v[1] for v in lp), max(v[1] for v in lp)
            if (mxx - mnx + 1) * (mxy - mny + 1) / n < 3:
                st = set(lp)
                ls = []
                for j in range(mny, mxy + 1, 1):
                    ls.append("".join("#" if (i, j) in st else " " for i in range(mnx, mxx + 1)))
                return "\n".join(ls)

    def solve_part_2(self, src):
        ls = self.parse(src)
        n = len(ls)
        for t in count(0):
            lp = [self._cal_pos(pt, t) for pt in ls]
            mnx, mxx = min(v[0] for v in lp), max(v[0] for v in lp)
            mny, mxy = min(v[1] for v in lp), max(v[1] for v in lp)
            if (mxx - mnx + 1) * (mxy - mny + 1) / n < 3:
                return t


if __name__ == "__main__":
    sol = Solver18D10()
    session = open('../.session').read().strip()
    cookies = {'session': session}

    src = requests.get(Solver18D10.INPUT_URL, cookies=cookies).text
    print(sol.solve_part_1(src))
    print(sol.solve_part_2(src))
