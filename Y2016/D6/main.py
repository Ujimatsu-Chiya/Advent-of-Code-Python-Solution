from collections import Counter

from utils import Solver, get_data


class Solver2016Day6(Solver):
    YEAR = 2016
    DAY = 6

    def __init__(self, src):
        self.ls = src.strip().split()
        self.ans1 = self.ans2 = None

    def run(self):
        self.ans1 = self.ans2 = ''
        n, m = len(self.ls), len(self.ls[0])
        for j in range(m):
            c = Counter(self.ls[i][j] for i in range(n))
            self.ans1 += max(c, key=c.get)
            self.ans2 += min(c, key=c.get)

    def solve_part_1(self):
        return self.ans1

    def solve_part_2(self):
        return self.ans2


if __name__ == "__main__":
    src = get_data(Solver2016Day6.YEAR, Solver2016Day6.DAY)
    sol = Solver2016Day6(src)
    sol.run()
    print(sol.solve_part_1())
    print(sol.solve_part_2())
