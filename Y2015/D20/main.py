from itertools import count

from utils import Solver, get_data
from tools import divisors_sigma
from math import exp, log


class Solver2015Day20(Solver):
    YEAR = 2015
    DAY = 20

    def __init__(self, src):
        self.n = int(src.strip())

    def solve_part_1(self):
        def robin_mx(n):
            t = log(log(n))
            return exp(0.5772156649015328606065120900824024310421) * n * t + 0.6483 * n / t

        l, r = 3, self.n
        while l < r:
            mid = (l + r) >> 1
            if robin_mx(mid) * 10 >= self.n:
                r = mid
            else:
                l = mid + 1

        for i in count(l):
            if divisors_sigma(i) * 10 >= self.n:
                return i

    def solve_part_2(self):
        M = 50
        for i in count(1):
            s = 0
            for j in range(1, M + 1):
                if i % j == 0:
                    s += i // j
            if s * 11 >= self.n:
                return i


if __name__ == "__main__":
    src = get_data(Solver2015Day20.YEAR, Solver2015Day20.DAY)
    sol = Solver2015Day20(src)
    print(sol.solve_part_1())
    print(sol.solve_part_2())
