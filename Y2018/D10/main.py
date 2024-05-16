import re
from itertools import count

from utils import Solver, get_data


class Solver2018Day10(Solver):
    YEAR = 2018
    DAY = 10

    def __init__(self, src):
        pat = re.compile(r'position=<\s*(-?\d+),\s*(-?\d+)>\s*velocity=<\s*(-?\d+),\s*(-?\d+)>')
        self.ls = [[(int(v[0]), int(v[1])), (int(v[2]), int(v[3]))] for v in pat.findall(src.strip())]
        self.ans1 = self.ans2 = None

    def _cal_pos(self, pt, tm):
        return tuple((p + v * tm) for p, v in zip(*pt))

    def run(self):
        n = len(self.ls)
        for t in count(0):
            lp = [self._cal_pos(pt, t) for pt in self.ls]
            mnx, mxx = min(v[0] for v in lp), max(v[0] for v in lp)
            mny, mxy = min(v[1] for v in lp), max(v[1] for v in lp)
            if (mxx - mnx + 1) * (mxy - mny + 1) / n < 3:
                st = set(lp)
                ls = []
                for j in range(mny, mxy + 1, 1):
                    ls.append("".join("#" if (i, j) in st else " " for i in range(mnx, mxx + 1)))
                self.ans1 = "\n".join(ls)
                self.ans2 = t
                break

    def solve_part_1(self):
        return self.ans1

    def solve_part_2(self):
        return self.ans2


if __name__ == "__main__":
    src = get_data(Solver2018Day10.YEAR, Solver2018Day10.DAY)
    sol = Solver2018Day10(src)
    sol.run()
    print(sol.solve_part_1())
    print(sol.solve_part_2())
