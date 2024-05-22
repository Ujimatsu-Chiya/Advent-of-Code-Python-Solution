from functools import lru_cache

from utils import Solver, get_data


class Solver2020Day19(Solver):
    YEAR = 2020
    DAY = 19

    def __init__(self, src):
        s1, s2 = src.strip().split('\n\n')
        ls = s1.split('\n')
        self.rules = {}
        for s in ls:
            l, r = s.split(':')
            l = int(l)
            if any(ch.isalpha() for ch in r):
                self.rules[l] = eval(r)
            else:
                self.rules[l] = [list(map(int, s.strip().split())) for s in r.strip().split('|')]
        self.queries = s2.strip().split()

    @lru_cache(maxsize=None)
    def match(self, idx, s):
        if isinstance(self.rules[idx], str):
            return s == self.rules[idx]
        else:
            for rule in self.rules[idx]:
                if len(rule) == 1:
                    if self.match(rule[0], s):
                        return True
                else:
                    n = len(s)
                    f = [False for _ in range(n + 1)]
                    for i in range(1, n):
                        if self.match(rule[0], s[:i]):
                            f[i] = True
                    for i in range(1, len(rule) - 1):
                        g = [False for _ in range(n + 1)]
                        for r in range(1, n + 1):
                            for l in range(1, r):
                                if not g[r] and f[l] and self.match(rule[i], s[l:r]):
                                    g[r] = True
                        f = g
                    for i in range(1, n):
                        if f[i] and self.match(rule[-1], s[i:]):
                            return True
            return False

    def solve_part_1(self):
        self.match.cache_clear()
        ans = 0
        for s in self.queries:
            if self.match(0, s):
                ans += 1
        return ans

    def solve_part_2(self):
        self.match.cache_clear()
        self.rules[8] = [[42], [42, 8]]
        self.rules[11] = [[42, 31], [42, 11, 31]]
        ans = 0
        for s in self.queries:
            if self.match(0, s):
                ans += 1
        return ans


if __name__ == "__main__":
    src = get_data(Solver2020Day19.YEAR, Solver2020Day19.DAY)
    sol = Solver2020Day19(src)
    print(sol.solve_part_1())
    print(sol.solve_part_2())
