from collections import Counter, defaultdict
from itertools import pairwise

from utils import Solver, get_data


class Solver2021Day14(Solver):
    YEAR = 2021
    DAY = 14

    def __init__(self, src):
        self.queries, op_str = src.strip().split('\n\n')
        self.rules = {}
        for s in op_str.split('\n'):
            l, r = s.split(' -> ')
            self.rules[l] = r

    def _run(self, M):
        mp = Counter([c1 + c2 for c1, c2 in pairwise(self.queries)])
        for _ in range(M):
            mq = defaultdict(int)
            for c1, c2 in mp.keys():
                mq[c1 + self.rules[c1 + c2]] += mp[c1 + c2]
                mq[self.rules[c1 + c2] + c2] += mp[c1 + c2]
            mp = mq
        cnt = defaultdict(int)
        cnt[self.queries[0]] += 1
        cnt[self.queries[-1]] += 1
        for s, val in mp.items():
            cnt[s[0]] += val
            cnt[s[1]] += val
        v = [x >> 1 for x in cnt.values()]
        return max(v) - min(v)

    def solve_part_1(self):
        return self._run(10)

    def solve_part_2(self):
        return self._run(40)


if __name__ == "__main__":
    src = get_data(Solver2021Day14.YEAR, Solver2021Day14.DAY)
    sol = Solver2021Day14(src)
    print(sol.solve_part_1())
    print(sol.solve_part_2())
