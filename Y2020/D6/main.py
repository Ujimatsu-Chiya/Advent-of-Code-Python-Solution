from utils import Solver, get_data
from collections import Counter


class Solver2020Day6(Solver):
    YEAR = 2020
    DAY = 6

    def __init__(self, src):
        self.queries = src.strip().split('\n\n')

    def solve_part_1(self):
        ans = 0
        for u in self.queries:
            ans += len(set(u.replace("\n", "")))
        return ans

    def solve_part_2(self):
        ans = 0
        for g in self.queries:
            sz = g.count('\n') + 1
            v = Counter(g.replace("\n", "")).values()
            ans += list(v).count(sz)
        return ans


if __name__ == "__main__":
    src = get_data(Solver2020Day6.YEAR, Solver2020Day6.DAY)
    sol = Solver2020Day6(src)
    print(sol.solve_part_1())
    print(sol.solve_part_2())
