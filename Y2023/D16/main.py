from collections import deque

from utils import Solver, get_data


class Solver2023Day16(Solver):
    YEAR = 2023
    DAY = 16

    def __init__(self, src):
        self.mp = src.strip().split()

    def _run(self, st):
        dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        trans = {('\\', 0): [3], ('\\', 1): [2], ('\\', 2): [1], ('\\', 3): [0],
                 ('/', 0): [1], ('/', 1): [0], ('/', 2): [3], ('/', 3): [2],
                 ('|', 0): [0], ('|', 1): [0, 2], ('|', 2): [2], ('|', 3): [0, 2],
                 ('-', 0): [1, 3], ('-', 1): [1], ('-', 2): [1, 3], ('-', 3): [3],
                 ('.', 0): [0], ('.', 1): [1], ('.', 2): [2], ('.', 3): [3]}
        n, m = len(self.mp), len(self.mp[0])
        vis = [[[False for _ in range(4)] for _ in range(m)] for _ in range(n)]
        vis[st[0]][st[1]][st[2]] = True
        q = deque([st])
        while len(q) > 0:
            x, y, p = q.popleft()
            for np in trans[self.mp[x][y], p]:
                nx, ny = x + dirs[np][0], y + dirs[np][1]
                if 0 <= nx < n and 0 <= ny < m and not vis[nx][ny][np]:
                    vis[nx][ny][np] = True
                    q.append([nx, ny, np])
        return sum(sum(vis[i][j]) > 0 for i in range(n) for j in range(m))

    def solve_part_1(self):
        return self._run([0, 0, 1])

    def solve_part_2(self):
        n, m = len(self.mp), len(self.mp[0])
        init = [[0, j, 2] for j in range(m)] + [[n - 1, j, 0] for j in range(m)] + \
               [[i, 0, 1] for i in range(n)] + [[i, m - 1, 3] for i in range(n)]
        return max(self._run(st) for st in init)


if __name__ == "__main__":
    src = get_data(Solver2023Day16.YEAR, Solver2023Day16.DAY)
    sol = Solver2023Day16(src)
    print(sol.solve_part_1())
    print(sol.solve_part_2())
