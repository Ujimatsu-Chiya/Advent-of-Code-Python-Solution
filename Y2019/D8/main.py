from collections import deque
from itertools import permutations
from utils import Solver, get_data


class Solver2019Day8(Solver):
    YEAR = 2019
    DAY = 8

    def __init__(self, src):
        self.s = src.strip()
        self.ans1 = self.ans2 = None

    def run(self):
        N, M = 6, 25
        a = [self.s[i:i + N * M] for i in range(0, len(self.s), N * M)][::-1]
        s = min(a, key=lambda s: s.count('0'))
        self.ans1 = s.count('1') * s.count('2')
        b = a[0]
        for s in a[1:]:
            b = "".join([c1 if c1 != '2' else c2 for c1, c2 in zip(s, b)])
        self.ans2 = "\n".join(b[i:i + M] for i in range(0, len(b), M)).replace('0', ' ').replace('1', '#')

    def solve_part_1(self):
        return self.ans1

    def solve_part_2(self):
        return self.ans2


if __name__ == "__main__":
    src = get_data(Solver2019Day8.YEAR, Solver2019Day8.DAY)
    sol = Solver2019Day8(src)
    sol.run()
    print(sol.solve_part_1())
    print(sol.solve_part_2())
