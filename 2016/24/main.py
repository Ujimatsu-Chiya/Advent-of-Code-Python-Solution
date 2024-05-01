from queue import Queue

from utils import Solver, get_data


class Solver2016Day24(Solver):
    YEAR = 2016
    DAY = 24
    dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]

    def parse(self, src):
        return src.strip().split()

    def _bfs(self, mp, sx, sy):
        n, m = len(mp), len(mp[0])
        q = Queue()
        q.put((sx, sy))
        d = [[-1 for _ in range(m)] for _ in range(n)]
        d[sx][sy] = 0
        while q.qsize() > 0:
            sx, sy = q.get()
            for dx, dy in self.dirs:
                x, y = sx + dx, sy + dy
                if 0 <= x < n and 0 <= y < m and mp[x][y] != '#' and d[x][y] == -1:
                    d[x][y] = d[sx][sy] + 1
                    q.put((x, y))
        return d

    def _solve(self, mp):
        n, m = len(mp), len(mp[0])
        pos = {}
        for i in range(n):
            for j in range(m):
                if mp[i][j].isdigit():
                    pos[int(mp[i][j])] = (i, j)
        o = int(max(pos.keys())) + 1
        g = [[0 for _ in range(o)] for _ in range(o)]
        for i in range(o):
            d = self._bfs(mp, pos[i][0], pos[i][1])
            for j in range(o):
                g[i][j] = d[pos[j][0]][pos[j][1]]
        inf = sum(sum(v) for v in g) + 1
        f = [[inf for _ in range(o)] for _ in range(1 << o)]
        f[1 << 0][0] = 0
        for st in range(1, 1 << o):
            for i in range(o):
                if f[st][i] != inf:
                    for j in range(o):
                        if not (st >> j & 1):
                            f[st | 1 << j][j] = min(f[st | 1 << j][j], f[st][i] + g[i][j])
        return g, f

    def solve_part_1(self, src):
        mp = self.parse(src)
        _, f = self._solve(mp)
        return min(f[-1])

    def solve_part_2(self, src):
        mp = self.parse(src)
        g, f = self._solve(mp)
        return min(f[-1][i] + g[i][0] for i in range(len(g)))

if __name__ == "__main__":
    sol = Solver2016Day24()
    src = get_data(Solver2016Day24.YEAR, Solver2016Day24.DAY)
    print(sol.solve_part_1(src))
    print(sol.solve_part_2(src))
