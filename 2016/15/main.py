import re
from itertools import count

from utils import Solver, get_data


class Solver2016Day15(Solver):
    YEAR = 2016
    DAY = 15

    def parse(self, src):
        pat = re.compile(r"Disc #(\d+) has (\d+) positions; at time=(\d+), it is at position (\d+).")
        ls = []
        for tp in pat.findall(src.strip()):
            ls.append([int(tp[1]), int(tp[3])])
        return ls

    def _solve(self, ls):
        for tm in count():
            if all((tm + i + 1 + t[1]) % t[0] == 0 for i, t in enumerate(ls)):
                return tm

    def solve_part_1(self, src):
        ls = self.parse(src)
        return self._solve(ls)

    def solve_part_2(self, src):
        ls = self.parse(src) + [[11, 0]]
        return self._solve(ls)


if __name__ == "__main__":
    sol = Solver2016Day15()
    src = get_data(Solver2016Day15.YEAR, Solver2016Day15.DAY)
    print(sol.solve_part_1(src))
    print(sol.solve_part_2(src))
