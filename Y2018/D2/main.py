from collections import Counter

from utils import Solver, get_data


class Solver2018Day2(Solver):
    YEAR = 2018
    DAY = 2

    def __init__(self, src):
        self.queries = src.strip().split()

    def solve_part_1(self):
        v_list = [Counter(s).values() for s in self.queries]
        c2 = sum(1 for v in v_list if 2 in v)
        c3 = sum(1 for v in v_list if 3 in v)
        return c2 * c3

    def solve_part_2(self):
        ls = self.queries
        a = []
        for i in range(len(ls)):
            for j in range(i):
                a.append([len([1 for k in range(len(ls[j])) if ls[i][k] != ls[j][k]]), i, j])
        a.sort()
        x, y = a[0][1:]
        return "".join(ls[x][i] for i in range(len(ls[x])) if ls[x][i] == ls[y][i])


if __name__ == "__main__":
    src = get_data(Solver2018Day2.YEAR, Solver2018Day2.DAY)
    sol = Solver2018Day2(src)
    print(sol.solve_part_1())
    print(sol.solve_part_2())
