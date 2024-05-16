from itertools import count

from utils import Solver, get_data


class Solver2016Day18(Solver):
    YEAR = 2016
    DAY = 18

    def __init__(self, src):
        self.ls = [int(ch == '^') for ch in src.strip()]
        self.ans1 = self.ans2 = None

    def run(self):
        def trans(ls):
            return [0] + [int(sum(ls[i - 1:i + 2]) == 2 and ls[i] == 1 or
                              sum(ls[i - 1:i + 2]) == 1 and ls[i] == 0) for i in range(1, m + 1)] + [0]

        m = len(self.ls)
        n1 = 40
        n2 = 400000
        ls = [0] + self.ls + [0]
        self.ans1 = 0
        for _ in range(n1):
            self.ans1 += m - sum(ls)
            ls = trans(ls)
        self.ans2 = self.ans1
        for _ in range(n2 - n1):
            self.ans2 += m - sum(ls)
            ls = trans(ls)

    def solve_part_1(self):
        return self.ans1

    def solve_part_2(self):
        return self.ans2


if __name__ == "__main__":
    src = get_data(Solver2016Day18.YEAR, Solver2016Day18.DAY)
    sol = Solver2016Day18(src)
    sol.run()
    print(sol.solve_part_1())
    print(sol.solve_part_2())
