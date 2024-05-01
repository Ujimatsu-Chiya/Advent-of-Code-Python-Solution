import hashlib
from itertools import count

from utils import Solver, get_data


class Solver2015Day4(Solver):
    YEAR = 2015
    DAY = 4

    def parse(self, src):
        return src.strip()

    def _solve(self, s, prefix):
        for i in count(1):
            md5 = hashlib.md5((s + str(i)).encode())
            if md5.hexdigest().startswith(prefix):
                return i

    def solve_part_1(self, src):
        s = self.parse(src)
        return self._solve(s, '0' * 5)

    def solve_part_2(self, src):
        s = self.parse(src)
        return self._solve(s, '0' * 6)


if __name__ == "__main__":
    sol = Solver2015Day4()
    src = get_data(Solver2015Day4.YEAR, Solver2015Day4.DAY)
    print(sol.solve_part_1(src))
    print(sol.solve_part_2(src))
