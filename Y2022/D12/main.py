from collections import deque

from utils import Solver, get_data


class Solver2022Day12(Solver):
    YEAR = 2022
    DAY = 12

    def __init__(self, src):
        self.mp = [list(s) for s in src.strip().split()]
        self.ans1 = self.ans2 = None

    def run(self):
        n, m = len(self.mp), len(self.mp[0])
        for i in range(n):
            for j in range(m):
                if self.mp[i][j] == 'S':
                    st = (i, j)
                    self.mp[i][j] = 'a'
                elif self.mp[i][j] == 'E':
                    ed = (i, j)
                    self.mp[i][j] = 'z'
        q = deque([ed])
        dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        d = [[-1 for _ in range(m)] for _ in range(n)]
        d[ed[0]][ed[1]] = 0
        while len(q) > 0:
            sx, sy = q.popleft()
            for dx, dy in dirs:
                x, y = sx + dx, sy + dy
                if 0 <= x < n and 0 <= y < m and d[x][y] == -1 and ord(self.mp[x][y]) >= ord(self.mp[sx][sy]) - 1:
                    d[x][y] = d[sx][sy] + 1
                    q.append((x, y))
        self.ans1 = d[st[0]][st[1]]
        self.ans2 = min(d[i][j] for i in range(n) for j in range(m) if self.mp[i][j] == 'a' and d[i][j] != -1)

    def solve_part_1(self):
        return self.ans1

    def solve_part_2(self):
        return self.ans2


if __name__ == "__main__":
    src = get_data(Solver2022Day12.YEAR, Solver2022Day12.DAY)
    sol = Solver2022Day12(src)
    sol.run()
    print(sol.solve_part_1())
    print(sol.solve_part_2())
