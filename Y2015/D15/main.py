import re

from utils import Solver, get_data


class Solver2015Day15(Solver):
    YEAR = 2015
    DAY = 15

    def __init__(self, src):
        pat = re.compile(
            r"(\w+): capacity (-?\d+), durability (-?\d+), flavor (-?\d+), texture (-?\d+), calories (\d+)")
        self.ingredients = [list(map(int, t[1:])) for t in pat.findall(src.strip())]
        self.ans1 = self.ans2 = None

    def run(self):
        self.ans1 = self.ans2 = -1
        ls = self.ingredients
        for i in range(100 + 1):
            for j in range(100 - i + 1):
                for k in range(100 - i - j + 1):
                    l = 100 - i - j - k
                    v = [max(i * ls[0][p] + j * ls[1][p] + k * ls[2][p] + l * ls[3][p], 0) for p in range(5)]
                    w = v[0] * v[1] * v[2] * v[3]
                    self.ans1 = max(self.ans1, w)
                    if v[4] == 500:
                        self.ans2 = max(self.ans2, w)

    def solve_part_1(self):
        return self.ans1

    def solve_part_2(self):
        return self.ans2


if __name__ == "__main__":
    src = get_data(Solver2015Day15.YEAR, Solver2015Day15.DAY)
    sol = Solver2015Day15(src)
    sol.run()
    print(sol.solve_part_1())
    print(sol.solve_part_2())
