import re
from itertools import count

from tools import CRT
from utils import Solver, get_data


class Solver2016Day15(Solver):
    YEAR = 2016
    DAY = 15

    def __init__(self, src):
        pat = re.compile(r"Disc #(\d+) has (\d+) positions; at time=(\d+), it is at position (\d+).")
        self.discs = [[int(tp[1]), int(tp[3])] for tp in pat.findall(src.strip())]

    def _solve(self, ls):
        a_list = ((-t[1] - i - 1) % t[0] for i, t in enumerate(ls))
        m_list = [t[0] for t in ls]
        return CRT(a_list, m_list)

    def solve_part_1(self):
        return self._solve(self.discs)

    def solve_part_2(self):
        return self._solve(self.discs + [[11, 0]])


if __name__ == "__main__":
    src = get_data(Solver2016Day15.YEAR, Solver2016Day15.DAY)
    sol = Solver2016Day15(src)
    print(sol.solve_part_1())
    print(sol.solve_part_2())
