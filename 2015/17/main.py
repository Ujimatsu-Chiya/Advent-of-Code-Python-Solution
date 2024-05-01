from utils import Solver, get_data


class Solver2015Day17(Solver):
    YEAR = 2015
    DAY = 17

    def parse(self, src):
        return list(map(int, src.strip().split()))

    def solve_part_1(self, src):
        ls = self.parse(src)
        M = 150
        f = [0 for _ in range(M + 1)]
        f[0] = 1
        for x in ls:
            for j in range(M, x - 1, -1):
                f[j] += f[j - x]
        return f[M]

    def solve_part_2(self, src):
        ls = self.parse(src)
        M = 150
        f = [0 for _ in range(M + 1)]
        g = [len(ls) + 1 for _ in range(M + 1)]
        f[0] = 1
        g[0] = 0
        for x in ls:
            for j in range(M, x - 1, -1):
                if g[j] > g[j - x] + 1:
                    g[j] = g[j - x] + 1
                    f[j] = f[j - x]
                elif g[j] == g[j - x] + 1:
                    f[j] += f[j - x]
        return f[M]


if __name__ == "__main__":
    sol = Solver2015Day17()
    src = get_data(Solver2015Day17.YEAR, Solver2015Day17.DAY)
    print(sol.solve_part_1(src))
    print(sol.solve_part_2(src))
