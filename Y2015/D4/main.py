from itertools import count

from tools import md5_digest
from utils import Solver, get_data


class Solver2015Day4(Solver):
    YEAR = 2015
    DAY = 4

    def __init__(self, src):
        self.s = src.strip()

    def _solve(self, s, prefix):
        for i in count(1):
            if md5_digest(s + str(i)).startswith(prefix):
                return i

    def solve_part_1(self):
        return self._solve(self.s, '0' * 5)

    def solve_part_2(self):
        return self._solve(self.s, '0' * 6)


if __name__ == "__main__":
    src = get_data(Solver2015Day4.YEAR, Solver2015Day4.DAY)
    sol = Solver2015Day4(src)
    print(sol.solve_part_1())
    print(sol.solve_part_2())
