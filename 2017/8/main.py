from collections import defaultdict

from utils import Solver, get_data


class Solver2017Day8(Solver):
    YEAR = 2017
    DAY = 8

    def parse(self, src):
        ls = []
        for s in src.strip().split('\n'):
            l, r = s.split(' if ')
            tp = l.strip().split()
            if tp[1] == "inc":
                ls.append([tp[0], int(tp[2]), r.strip()])
            else:
                ls.append([tp[0], -int(tp[2]), r.strip()])
        return ls

    def solve_part_1(self, src):
        ls = self.parse(src)
        mp = defaultdict(int)
        for reg, delta, cond in ls:
            if eval(cond, mp):
                mp[reg] += delta
        return max(x for x in mp.values() if isinstance(x, int))

    def solve_part_2(self, src):
        ls = self.parse(src)
        ans = 0
        mp = defaultdict(int)
        for reg, delta, cond in ls:
            if eval(cond, mp):
                mp[reg] += delta
                ans = max(ans, mp[reg])
        return ans


if __name__ == "__main__":
    sol = Solver2017Day8()
    src = get_data(Solver2017Day8.YEAR, Solver2017Day8.DAY)
    print(sol.solve_part_1(src))
    print(sol.solve_part_2(src))
