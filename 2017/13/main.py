import re
from itertools import count

from utils import Solver, get_data


class Solver2017Day13(Solver):
    YEAR = 2017
    DAY = 13

    def parse(self, src):
        pattern = r"(\d+): (\d+)"
        return [list(map(int, v)) for v in re.findall(pattern, src.strip())]

    def solve_part_1(self, src):
        a = self.parse(src)
        ans = 0
        for k, v in a:
            if k % (2 * (v - 1)) == 0:
                ans += k * v
        return ans

    def solve_part_2(self, src):
        a = self.parse(src)
        for t in count(0):
            if all((t + k) % (2 * (v - 1)) != 0 for k, v in a):
                return t


if __name__ == "__main__":
    sol = Solver2017Day13()
    src = get_data(Solver2017Day13.YEAR, Solver2017Day13.DAY)
    print(sol.solve_part_1(src))
    print(sol.solve_part_2(src))
