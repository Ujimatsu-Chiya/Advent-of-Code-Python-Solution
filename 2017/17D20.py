import re
from collections import Counter
from itertools import count

import requests

from utils import Solver


class Solver17D20(Solver):
    INPUT_URL = 'https://adventofcode.com/2017/day/20/input'

    def parse(self, src):
        pat = re.compile(r"p=<(-?\d+),(-?\d+),(-?\d+)>,\s*v=<(-?\d+),(-?\d+),(-?\d+)>,\s*a=<(-?\d+),(-?\d+),(-?\d+)>")
        ls = []
        for tp in pat.findall(src.strip()):
            p = tuple(map(int, tp[0:3]))
            v = tuple(map(int, tp[3:6]))
            a = tuple(map(int, tp[6:9]))
            ls.append((p, v, a))
        return ls

    def _cal_pos(self, pt, tm):
        return tuple((p + v * tm + a * (tm + 1) * tm // 2) for p, v, a in zip(*pt))

    def solve_part_1(self, src):

        def dis(pt, tm):
            return sum(abs(p) for p in self._cal_pos(pt, tm))

        ls = self.parse(src)
        t = 1
        cnt = 0
        pre = []
        while True:
            a = sorted([[dis(ls[i], t), i] for i in range(len(ls))])
            b = [v[1] for v in a]
            if b == pre:
                cnt += 1
                if cnt == 5:
                    break
            else:
                cnt = 0
                pre = b

            t *= 10
        return pre[0]

    def solve_part_2(self, src):
        ls = sorted(self.parse(src))
        pre = len(ls)
        cnt = 0
        for tm in count():
            lt = [self._cal_pos(pt, tm) for pt in ls]
            c = Counter(lt)
            ls = [ls[i] for i in range(len(ls)) if c[lt[i]] == 1]
            if len(ls) == pre:
                cnt += 1
                if cnt == 1000:
                    break
            else:
                pre = len(ls)
                cnt = 0
        return len(ls)


if __name__ == "__main__":
    sol = Solver17D20()
    session = open('../.session').read().strip()
    cookies = {'session': session}

    src = requests.get(Solver17D20.INPUT_URL, cookies=cookies).text
    print(sol.solve_part_1(src))
    print(sol.solve_part_2(src))
