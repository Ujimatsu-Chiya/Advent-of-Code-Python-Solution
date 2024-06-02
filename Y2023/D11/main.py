from utils import Solver, get_data
from itertools import combinations

class Solver2023Day11(Solver):
    YEAR = 2023
    DAY = 11

    def __init__(self, src):
        self.mp = src.strip().split('\n')

    def _run(self, M):
        n, m = len(self.mp), len(self.mp[0])
        cx = [0 for _ in range(n)]
        cy = [0 for _ in range(m)]
        for i in range(n):
            for j in range(m):
                if self.mp[i][j] == '#':
                    cx[i] += 1
                    cy[j] += 1

        kx = [int(w == 0) for w in cx]
        ky = [int(w == 0) for w in cy]
        for i in range(1, n):
            kx[i] += kx[i - 1]
        for j in range(1, m):
            ky[j] += ky[j - 1]
        ls = []
        for i in range(n):
            for j in range(m):
                if self.mp[i][j] == '#':
                    ls.append((i + kx[i] * M, j + ky[j] * M))
        ans = 0
        for pa, pb in combinations(ls, 2):
            ans += abs(pa[0] - pb[0]) + abs(pa[1] - pb[1])
        return ans

    def solve_part_1(self):
        return self._run(1)

    def solve_part_2(self):
        M = 1000000
        return self._run(M - 1)


if __name__ == "__main__":
    src = get_data(Solver2023Day11.YEAR, Solver2023Day11.DAY)
    sol = Solver2023Day11(src)
    print(sol.solve_part_1())
    print(sol.solve_part_2())
