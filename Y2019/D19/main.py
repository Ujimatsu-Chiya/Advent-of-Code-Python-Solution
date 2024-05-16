from tools import IntCodeComputer
from utils import Solver, get_data
from itertools import count


class Solver2019Day19(Solver):
    YEAR = 2019
    DAY = 19

    def __init__(self, src):
        self.ops = list(map(int, src.strip().split(',')))
        self.ans1 = self.ans2 = None

    def run(self):
        def que(i, j):
            p = IntCodeComputer(self.ops, [i, j])
            return p.get_output()

        for i in count(1):
            pt = None
            for k in range(0, i + 1):
                if que(k, i):
                    pt = (k, i)
                if que(i, k):
                    pt = (i, k)
            if pt:
                break
        M = 100
        ls = [[-1, -1] for _ in range(pt[0])]
        ls[0] = [0, 1]
        k, l, r = pt[0], pt[1], pt[1]
        for x in range(k, k + 2000):
            while not que(x, l):
                l += 1
            while que(x, r):
                r += 1
            ls.append([l, r])
            if len(ls) >= M and ls[-1][0] + M <= ls[-M][1]:
                self.ans2 = (x - M + 1) * 10000 + ls[-1][0]
                break
        N = 50
        self.ans1 = 0
        for i in range(N):
            for j in range(ls[i][0], ls[i][1]):
                if j < N:
                    self.ans1 += 1

    def solve_part_1(self):
        return self.ans1

    def solve_part_2(self):
        return self.ans2


if __name__ == "__main__":
    src = get_data(Solver2019Day19.YEAR, Solver2019Day19.DAY)
    sol = Solver2019Day19(src)
    sol.run()
    print(sol.solve_part_1())
    print(sol.solve_part_2())
