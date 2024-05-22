import re

from utils import Solver, get_data
from itertools import chain
from tools import transpose
from collections import defaultdict
from functools import reduce
import operator


class Solver2020Day16(Solver):
    YEAR = 2020
    DAY = 16

    def __init__(self, src):
        s1, s2, s3 = src.strip().split('\n\n')
        pat1 = re.compile(r'([a-zA-Z ]+):\s+(.+)*')
        self.rules = {}
        for name, s in pat1.findall(s1):
            tp = s.split(" or ")
            ls = []
            for s in tp:
                ls.append(list(map(int, s.split('-'))))
            self.rules[name] = sorted(ls)

        self.your = list(map(int, s2.split('\n')[1].split(',')))
        self.nearby = [list(map(int, s.split(','))) for s in s3.split('\n')[1:]]
        self.ans1 = self.ans2 = None

    def run(self):
        self.ans1 = 0
        values = list(chain.from_iterable(self.rules.values()))
        valid = []
        for ticket in self.nearby:
            ok = True
            for x in ticket:
                if all(not l <= x <= r for l, r in values):
                    self.ans1 += x
                    ok = False
            if ok:
                valid.append(ticket)
        valid = transpose(valid + [self.your])
        info = defaultdict(list)
        for name, ranges in self.rules.items():
            for i, vals in enumerate(valid):
                if all(any(l <= x <= r for l, r in ranges) for x in vals):
                    info[name].append(i)
        match = {}
        while len(info) > 0:
            for k, v in info.items():
                if len(v) == 1:
                    match[k] = v[0]
            for k in match.keys():
                if k in info.keys():
                    info.pop(k)
            for k in info.keys():
                info[k] = [x for x in info[k] if x not in match.values()]
        self.ans2 = reduce(operator.mul, [self.your[v] for k, v in match.items() if k.startswith('departure')])

    def solve_part_1(self):
        return self.ans1

    def solve_part_2(self):
        return self.ans2


if __name__ == "__main__":
    src = get_data(Solver2020Day16.YEAR, Solver2020Day16.DAY)
    sol = Solver2020Day16(src)
    sol.run()
    print(sol.solve_part_1())
    print(sol.solve_part_2())
