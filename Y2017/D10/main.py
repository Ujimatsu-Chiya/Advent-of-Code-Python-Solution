import operator
from functools import reduce

from utils import Solver, get_data


class Solver2017Day10(Solver):
    YEAR = 2017
    DAY = 10

    def __init__(self, src):
        self.s= src.strip()

    def _solve(self, a):
        M = 256
        b = list(range(M))
        p = 0
        for skip_size, x in enumerate(a):
            if p + x <= M:
                l, m, r = b[:p], b[p:p + x], b[p + x:]
                b = l + list(reversed(m)) + r
            else:
                rev = list(reversed(b[p:] + b[:x - (M - p)]))
                rest = b[x - (M - p):p]
                b = rev[- (x - (M - p)):] + rest + rev[:-(x - (M - p))]
            p = (p + x + skip_size) % M
            skip_size += 1
        return b

    def solve_part_1(self):
        a = list(map(int, self.s.split(',')))
        b = self._solve(a)
        return b[0] * b[1]

    def solve_part_2(self):
        a = [ord(x) for x in self.s]
        a = (a + [17, 31, 73, 47, 23]) * 64
        b = self._solve(a)
        t = [reduce(operator.xor, b[i:i + 16]) for i in range(0, len(b), 16)]
        return "".join("{:02x}".format(x) for x in t)


if __name__ == "__main__":
    src = get_data(Solver2017Day10.YEAR, Solver2017Day10.DAY)
    sol = Solver2017Day10(src)
    print(sol.solve_part_1())
    print(sol.solve_part_2())
