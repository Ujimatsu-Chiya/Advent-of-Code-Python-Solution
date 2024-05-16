import re
from itertools import count

from utils import Solver, get_data


class Solver2017Day13(Solver):
    YEAR = 2017
    DAY = 13

    def __init__(self, src):
        pat = re.compile(r"(\d+): (\d+)")
        self.a = [list(map(int, v)) for v in pat.findall(src.strip())]

    def solve_part_1(self):
        ans = 0
        for k, v in self.a:
            if k % (2 * (v - 1)) == 0:
                ans += k * v
        return ans

    def solve_part_2(self):
        for t in count(0):
            if all((t + k) % (2 * (v - 1)) != 0 for k, v in self.a):
                return t


if __name__ == "__main__":
    src = get_data(Solver2017Day13.YEAR, Solver2017Day13.DAY)
    sol = Solver2017Day13(src)
    print(sol.solve_part_1())
    print(sol.solve_part_2())
