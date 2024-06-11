from itertools import count

from tools import md5_digest
from utils import Solver, get_data


# class Solver2015Day4(Solver):
#     YEAR = 2015
#     DAY = 4
#
#     def __init__(self, src):
#         self.s = src.strip()
#
#     def _solve(self, s, prefix):
#         for i in count(1):
#             if md5_digest(s + str(i)).startswith(prefix):
#                 return i
#
#     def solve_part_1(self):
#         return self._solve(self.s, '0' * 5)
#
#     def solve_part_2(self):
#         return self._solve(self.s, '0' * 6)

class Solver2015Day4(Solver):
    YEAR = 2015
    DAY = 4

    def __init__(self, src):
        self.s = src.strip()
        self.ans1 = self.ans2 = None

    def run(self):
        prefix1 = "00000"
        prefix2 = prefix1 + "0"
        for i in count(1):
            t = md5_digest(self.s + str(i))
            if t.startswith(prefix1):
                if self.ans1 is None:
                    self.ans1 = i
                if t.startswith(prefix2):
                    self.ans2 = i
                    break

    def solve_part_1(self):
        return self.ans1

    def solve_part_2(self):
        return self.ans2


if __name__ == "__main__":
    from time import time

    st = time()
    src = get_data(Solver2015Day4.YEAR, Solver2015Day4.DAY)
    sol = Solver2015Day4(src)
    sol.run()
    print(sol.solve_part_1())
    print(sol.solve_part_2())
    print(time() - st)
