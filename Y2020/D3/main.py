from functools import reduce
import operator

from utils import Solver, get_data


class Solver2020Day3(Solver):
    YEAR = 2020
    DAY = 3

    def __init__(self, src):
        self.mp = src.strip().split()

    def cal(self, x, y):
        return sum(1 for i in range((len(self.mp) + x - 1) // x) if self.mp[i * x][i * y % len(self.mp[0])] == '#')

    def solve_part_1(self):
        return self.cal(1, 3)

    def solve_part_2(self):
        queries = [[1, 1], [1, 3], [1, 5], [1, 7], [2, 1]]
        return reduce(operator.mul, [self.cal(x, y) for x, y in queries])


if __name__ == "__main__":
    src = get_data(Solver2020Day3.YEAR, Solver2020Day3.DAY)
    sol = Solver2020Day3(src)
    print(sol.solve_part_1())
    print(sol.solve_part_2())
