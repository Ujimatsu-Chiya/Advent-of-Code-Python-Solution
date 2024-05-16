from utils import Solver, get_data


class Solver2015Day17(Solver):
    YEAR = 2015
    DAY = 17

    def __init__(self, src):
        self.containers = list(map(int, src.strip().split()))

    def solve_part_1(self):
        M = 150
        f = [0 for _ in range(M + 1)]
        f[0] = 1
        for x in self.containers:
            for j in range(M, x - 1, -1):
                f[j] += f[j - x]
        return f[M]

    def solve_part_2(self):
        M = 150
        f = [0 for _ in range(M + 1)]
        g = [len(self.containers) + 1 for _ in range(M + 1)]
        f[0] = 1
        g[0] = 0
        for x in self.containers:
            for j in range(M, x - 1, -1):
                if g[j] > g[j - x] + 1:
                    g[j] = g[j - x] + 1
                    f[j] = f[j - x]
                elif g[j] == g[j - x] + 1:
                    f[j] += f[j - x]
        return f[M]


if __name__ == "__main__":
    src = get_data(Solver2015Day17.YEAR, Solver2015Day17.DAY)
    sol = Solver2015Day17(src)
    print(sol.solve_part_1())
    print(sol.solve_part_2())
