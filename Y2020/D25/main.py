from utils import Solver, get_data
from itertools import count


class Solver2020Day25(Solver):
    YEAR = 2020
    DAY = 25

    def __init__(self, src):
        self.a = [int(s) for s in src.strip().split()]

    def solve_part_1(self):
        mod = 20201227
        x = 1
        for e in count(1):
            x = x * 7 % mod
            if x in self.a:
                self.a.remove(x)
                y = self.a[0]
                return pow(y, e, mod)

    def solve_part_2(self):
        pass


if __name__ == "__main__":
    src = get_data(Solver2020Day25.YEAR, Solver2020Day25.DAY)
    sol = Solver2020Day25(src)
    print(sol.solve_part_1())
    print(sol.solve_part_2())
