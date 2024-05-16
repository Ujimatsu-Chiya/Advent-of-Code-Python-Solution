from collections import defaultdict

from utils import Solver, get_data


class Solver2017Day8(Solver):
    YEAR = 2017
    DAY = 8

    def __init__(self, src):
        self.ls = []
        for s in src.strip().split('\n'):
            l, r = s.split(' if ')
            tp = l.strip().split()
            self.ls.append([tp[0], int(tp[2]) if tp[1] == "inc" else -int(tp[2]), r.strip()])
        self.ans1 = self.ans2 = None

    def run(self):
        self.ans2 = 0
        mp = defaultdict(int)
        for reg, delta, cond in self.ls:
            if eval(cond, mp):
                mp[reg] += delta
                self.ans2 = max(self.ans2, mp[reg])
        self.ans1 = max(x for x in mp.values() if isinstance(x, int))

    def solve_part_1(self):
        return self.ans1

    def solve_part_2(self):
        return self.ans2


if __name__ == "__main__":
    src = get_data(Solver2017Day8.YEAR, Solver2017Day8.DAY)
    sol = Solver2017Day8(src)
    sol.run()
    print(sol.solve_part_1())
    print(sol.solve_part_2())
