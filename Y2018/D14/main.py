from itertools import count

from utils import Solver, get_data


class Solver2018Day14(Solver):
    YEAR = 2018
    DAY = 14

    def __init__(self, src):
        self.n = int(src.strip())

    def gen(self):
        a = [3, 7]
        p0, p1 = 0, 1
        for p in count():
            while p >= len(a):
                x = a[p0] + a[p1]
                if x >= 10:
                    a.append(1)
                    x -= 10
                a.append(x)
                p0 = (p0 + 1 + a[p0]) % len(a)
                p1 = (p1 + 1 + a[p1]) % len(a)
            yield a[p]

    def solve_part_1(self):
        g = self.gen()
        a = []
        for _ in range(self.n + 10):
            a.append(next(g))
        return "".join(map(str, a[-10:]))

    def solve_part_2(self):
        g = self.gen()
        b = [int(x) for x in str(self.n)]
        a = []
        while True:
            a.append(next(g))
            if a[-len(b):] == b:
                return len(a) - len(b)


if __name__ == "__main__":
    src = get_data(Solver2018Day14.YEAR, Solver2018Day14.DAY)
    sol = Solver2018Day14(src)
    print(sol.solve_part_1())
    print(sol.solve_part_2())
