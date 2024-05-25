from utils import Solver, get_data
from math import inf


class Solver2021Day7(Solver):
    YEAR = 2021
    DAY = 7

    def __init__(self, src):
        self.queries = list(map(int, src.strip().split(',')))

    def solve_part_1(self):
        a = sorted(self.queries)
        return sum(abs(x - a[len(a) >> 1]) for x in a)

    def solve_part_2(self):
        a = sorted(self.queries)
        ans = inf
        for i in range(a[0], a[-1] + 1):
            s = 0
            for x in a:
                v = abs(x - i)
                s += v * (v + 1) // 2
            ans = min(ans, s)
        return ans


if __name__ == "__main__":
    src = get_data(Solver2021Day7.YEAR, Solver2021Day7.DAY)
    sol = Solver2021Day7(src)
    print(sol.solve_part_1())
    print(sol.solve_part_2())
