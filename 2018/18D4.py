import re
from collections import Counter, defaultdict

import numpy as np
import requests

from utils import Solver


class Solver18D4(Solver):
    INPUT_URL = 'https://adventofcode.com/2018/day/4/input'

    def parse(self, src):
        pat = re.compile(
            r"\[(\d{4})-(\d{2})-(\d{2}) (\d{2}):(\d{2})\] (Guard #(\d+) begins shift|falls asleep|wakes up)")
        ls = []
        for t in pat.findall("\n".join(sorted(src.strip().split('\n')))):
            ls.append([int(t[4]), t[5] if len(t[6]) == 0 else int(t[6])])
        return ls

    def _solve(self, ls):
        ls = self.parse(src)
        mp = defaultdict(list)
        id = -1
        pre = -1
        for tm, op in ls:
            if isinstance(op, int):
                id = op
            elif op == 'falls asleep':
                pre = tm
            else:
                mp[id] += list(range(pre, tm))
        return mp

    def solve_part_1(self, src):
        ls = self.parse(src)
        mp = self._solve(ls)
        a = sorted([[len(v), k] for k, v in mp.items()], reverse=True)
        id = a[0][1]
        return Counter(mp[id]).most_common(1)[0][0] * id

    def solve_part_2(self, src):
        ls = self.parse(src)
        mp = self._solve(ls)
        a = sorted([[*list(reversed(Counter(v).most_common(1)[0])), k] for k, v in mp.items()], reverse=True)
        return a[0][1] * a[0][2]


if __name__ == "__main__":
    sol = Solver18D4()
    session = open('../.session').read().strip()
    cookies = {'session': session}

    src = requests.get(Solver18D4.INPUT_URL, cookies=cookies).text
    print(sol.solve_part_1(src))
    print(sol.solve_part_2(src))
