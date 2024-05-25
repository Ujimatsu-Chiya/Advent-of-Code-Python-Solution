from utils import Solver, get_data
from itertools import pairwise


class Solver2021Day1(Solver):
    YEAR = 2021
    DAY = 1

    def __init__(self, src):
        self.queries = list(map(int, src.strip().split()))

    def solve_part_1(self):
        return sum(1 for x, y in pairwise(self.queries) if x < y)

    def solve_part_2(self):
        a = [sum(self.queries[i-3:i]) for i in range(len(self.queries))]
        return sum(1 for x, y in pairwise(a) if x < y)


if __name__ == "__main__":
    src = get_data(Solver2021Day1.YEAR, Solver2021Day1.DAY)
    sol = Solver2021Day1(src)
    print(sol.solve_part_1())
    print(sol.solve_part_2())
