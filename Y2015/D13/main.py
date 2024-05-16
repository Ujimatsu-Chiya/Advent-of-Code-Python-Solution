import re
from itertools import permutations

from utils import Solver, get_data


class Solver2015Day13(Solver):
    YEAR = 2015
    DAY = 13

    def __init__(self, src):
        pat = re.compile(r"(\w+) would (lose|gain) (\d+) happiness units by sitting next to (\w+)\.")
        self.st, self.mp = set(), {}

        for p1, op, v, p2 in pat.findall(src.strip()):
            self.mp[p1, p2] = int(v) if op == 'gain' else -int(v)
            self.st |= {p1, p2}

    def _run(self, st, mp):
        ls = list(st)
        lt, ls = ls[:1], ls[1:]
        ans = 0
        n = len(st)
        for p in permutations(ls):
            t = lt + list(p) + lt
            ans = max(ans, sum(mp[t[i], t[i + 1]] + mp[t[i + 1], t[i]] for i in range(n)))
        return ans

    def solve_part_1(self):
        return self._run(self.st, self.mp)

    def solve_part_2(self):
        me = 'me'
        st, mp = self.st | {me}, self.mp.copy()
        for s in self.st:
            mp[s, me] = mp[me, s] = 0
        return self._run(st, mp)


if __name__ == "__main__":
    src = get_data(Solver2015Day13.YEAR, Solver2015Day13.DAY)
    sol = Solver2015Day13(src)
    print(sol.solve_part_1())
    print(sol.solve_part_2())
