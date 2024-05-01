import re

from utils import Solver, get_data


class Solver2017Day15(Solver):
    YEAR = 2017
    DAY = 15

    def parse(self, src):
        a = re.findall(r'\d+', src.strip())
        return list(map(int, a))

    def solve_part_1(self, src):
        a, b = self.parse(src)
        ma, mb = 16807, 48271
        mod = (1 << 31) - 1
        msk = (1 << 16) - 1
        M = 40000000
        ans = 0
        for i in range(M):
            a = a * ma % mod
            b = b * mb % mod
            if ((a - b) & msk) == 0:
                ans += 1
        return ans

    def solve_part_2(self, src):
        a, b = self.parse(src)
        ma, mb = 16807, 48271
        mod = (1 << 31) - 1
        msk = (1 << 16) - 1

        def gen(st, m, bit):
            x = st
            msk_now = (1 << bit) - 1
            while True:
                x = x * m % mod
                if (x & msk_now) == 0:
                    yield x

        A = gen(a, ma, 2)
        B = gen(b, mb, 3)
        M = 5000000
        ans = 0
        for i in range(M):
            a = next(A)
            b = next(B)
            if ((a - b) & msk) == 0:
                ans += 1
        return ans



if __name__ == "__main__":
    sol = Solver2017Day15()
    src = get_data(Solver2017Day15.YEAR, Solver2017Day15.DAY)
    print(sol.solve_part_1(src))
    print(sol.solve_part_2(src))
