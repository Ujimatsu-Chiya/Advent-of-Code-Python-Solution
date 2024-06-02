from itertools import count
from math import prod

from utils import Solver, get_data


class Solver2022Day8(Solver):
    YEAR = 2022
    DAY = 8

    def __init__(self, src):
        self.mp = [[int(ch) for ch in s] for s in src.strip().split()]

    def solve_part_1(self):
        n, m = len(self.mp), len(self.mp[0])

        def solve(mp):
            f = [[0 for _ in range(m)] for _ in range(n)]
            x = [-1 for _ in range(n)]
            y = [-1 for _ in range(m)]
            for i in range(n):
                for j in range(m):
                    if mp[i][j] > x[i] or mp[i][j] > y[j]:
                        f[i][j] = 1
                    x[i] = max(x[i], mp[i][j])
                    y[j] = max(y[j], mp[i][j])
            return f

        f1 = solve(self.mp)
        f2 = solve([v[::-1] for v in reversed(self.mp)])
        return sum(f1[i][j] | f2[n - 1 - i][m - 1 - j] for i in range(n) for j in range(m))

    def solve_part_2(self):
        n, m = len(self.mp), len(self.mp[0])
        dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        ans = 0
        for i in range(n):
            for j in range(m):
                ls = []
                for dx, dy in dirs:
                    for k in count(1):
                        x, y = i + dx * k, j + dy * k
                        if not (0 <= x < n and 0 <= y < m):
                            ls.append(k - 1)
                            break
                        elif self.mp[i][j] <= self.mp[x][y]:
                            ls.append(k)
                            break
                ans = max(ans, prod(ls))
        return ans
if __name__ == "__main__":
    src = get_data(Solver2022Day8.YEAR, Solver2022Day8.DAY)
    sol = Solver2022Day8(src)
    print(sol.solve_part_1())
    print(sol.solve_part_2())
