from collections import Counter

from utils import Solver, get_data


class Solver2018Day2(Solver):
    YEAR = 2018
    DAY = 2

    def parse(self, src):
        return src.strip().split()

    def solve_part_1(self, src):
        ls = self.parse(src)
        c2 = c3 = 0
        for s in ls:
            v = Counter(s).values()
            if 2 in v:
                c2 += 1
            if 3 in v:
                c3 += 1
        return c2 * c3

    def solve_part_2(self, src):
        ls = self.parse(src)
        a = []
        for i in range(len(ls)):
            for j in range(i):
                a.append([len([1 for k in range(len(ls[j])) if ls[i][k] != ls[j][k]]), i, j])
        a.sort()
        x, y = a[0][1:]
        return "".join(ls[x][i] for i in range(len(ls[x])) if ls[x][i] == ls[y][i])


if __name__ == "__main__":
    sol = Solver2018Day2()
    src = get_data(Solver2018Day2.YEAR, Solver2018Day2.DAY)
    print(sol.solve_part_1(src))
    print(sol.solve_part_2(src))
