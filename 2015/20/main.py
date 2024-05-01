from itertools import count

from utils import Solver, divisors_sigma, get_data


class Solver2015Day20(Solver):
    YEAR = 2015
    DAY = 20

    def parse(self, src):
        return int(src.strip())

    def solve_part_1(self, src):
        n = self.parse(src)
        for i in count(1):
            if divisors_sigma(i) * 10 >= n:
                return i

    def solve_part_2(self, src):
        n = self.parse(src)
        M = 50
        for i in count(1):
            s = 0
            for j in range(1, M + 1):
                if i % j == 0:
                    s += i // j
            if s * 11 >= n:
                return i


if __name__ == "__main__":
    sol = Solver2015Day20()
    src = get_data(Solver2015Day20.YEAR, Solver2015Day20.DAY)
    print(sol.solve_part_1(src))
    print(sol.solve_part_2(src))
