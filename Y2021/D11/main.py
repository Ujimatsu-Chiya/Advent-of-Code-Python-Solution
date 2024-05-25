from collections import deque
from itertools import count

from utils import Solver, get_data


class Solver2021Day11(Solver):
    YEAR = 2021
    DAY = 11

    def __init__(self, src):
        self.mp = [[int(ch) for ch in s] for s in src.strip().split()]
        self.ans1 = self.ans2 = None

    def run(self):
        mp = self.mp
        n, m = len(self.mp), len(self.mp[0])
        dirs = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
        T = 100
        self.ans1 = 0
        for r in count():
            mp = [[x + 1 for x in u] for u in mp]
            q = deque()
            vis = [[False for _ in range(m)] for _ in range(n)]
            for i in range(n):
                for j in range(m):
                    if mp[i][j] == 10:
                        q.append((i, j))
                        vis[i][j] = True
                        mp[i][j] = 0
            while len(q) > 0:
                sx, sy = q.popleft()
                for dx, dy in dirs:
                    x, y = sx + dx, sy + dy
                    if 0 <= x < n and 0 <= y < m and not vis[x][y]:
                        mp[x][y] += 1
                        if mp[x][y] == 10:
                            q.append((x, y))
                            vis[x][y] = True
                            mp[x][y] = 0
            val = sum(sum(u) for u in vis)
            if r < T:
                self.ans1 += val
            if val == n * m:
                self.ans2 = r + 1
                break

    def solve_part_1(self):
        return self.ans1

    def solve_part_2(self):
        return self.ans2


if __name__ == "__main__":
    src = get_data(Solver2021Day11.YEAR, Solver2021Day11.DAY)
    sol = Solver2021Day11(src)
    sol.run()
    print(sol.solve_part_1())
    print(sol.solve_part_2())
