from itertools import count

from tools import md5_digest
from utils import Solver, get_data


class Solver2016Day5(Solver):
    YEAR = 2016
    DAY = 5

    def __init__(self, src):
        self.s = src.strip()
        self.ans1 = self.ans2 = None

    def run(self):
        prefix = "00000"

        def gen():
            for i in count(1):
                t = md5_digest(self.s + str(i))
                if t.startswith(prefix):
                    yield t

        M = 8
        g = gen()
        a1 = []
        a2 = ['' for _ in range(M)]
        while True:
            if self.ans1 is not None and self.ans2 is not None:
                break
            t = next(g)
            c1, c2 = t[len(prefix)], t[len(prefix) + 1]
            a1.append(c1)
            if len(a1) == M:
                self.ans1 = "".join(a1)
            if c1.isdigit():
                p = int(c1)
                if p < M and a2[p] == '':
                    a2[p] = c2
                    if a2.count('') == 0:
                        self.ans2 = "".join(a2)

    def solve_part_1(self):
        return self.ans1

    def solve_part_2(self):
        return self.ans2


if __name__ == "__main__":
    src = get_data(Solver2016Day5.YEAR, Solver2016Day5.DAY)
    sol = Solver2016Day5(src)
    sol.run()
    print(sol.solve_part_1())
    print(sol.solve_part_2())
