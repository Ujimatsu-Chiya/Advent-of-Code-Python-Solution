from heapq import heappush, heappop

from utils import Solver, get_data
import numpy as np


class Solver2021Day15(Solver):
    YEAR = 2021
    DAY = 15

    def __init__(self, src):
        self.mp = [[int(ch) for ch in s] for s in src.strip().split()]

    def _run(self, mp):
        n, m = len(mp), len(mp[0])
        dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        d = [[-1 for _ in range(m)] for _ in range(n)]
        q = []
        heappush(q, (0, 0, 0))
        while len(q) > 0:
            dis, sx, sy = heappop(q)
            if d[sx][sy] == -1:
                d[sx][sy] = dis
                for dx, dy in dirs:
                    x, y = sx + dx, sy + dy
                    if 0 <= x < n and 0 <= y < m and d[x][y] == -1:
                        heappush(q, (dis + mp[x][y], x, y))
        return d[-1][-1]

    def solve_part_1(self):
        return self._run(self.mp)

    def solve_part_2(self):
        n, m = len(self.mp), len(self.mp[0])
        M = 5
        mp = np.zeros((n * M, m * M), dtype=int)
        for i in range(M):
            for j in range(M):
                mp[i * n:i * n + n, j * m:j * m + m] = np.array([[(x + i + j - 1) % 9 + 1 for x in u] for u in self.mp])
        return self._run(mp)


if __name__ == "__main__":
    src = get_data(Solver2021Day15.YEAR, Solver2021Day15.DAY)
    sol = Solver2021Day15(src)
    print(sol.solve_part_1())
    print(sol.solve_part_2())
