import re
from queue import Queue

from utils import Solver, get_data


class Solver2016Day22(Solver):
    YEAR = 2016
    DAY = 22
    dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]

    def __init__(self, src):
        pat = re.compile(r"node-x(\d+)-y(\d+)\s+(\d+)T\s+(\d+)T\s+(\d+)T\s+(\d+)%")
        ls = [[int(v[0]), int(v[1]), int(v[3]), int(v[4])] for v in pat.findall(src.strip())]
        n = max(v[0] for v in ls) + 1
        m = max(v[1] for v in ls) + 1
        self.used = [[0 for _ in range(m)] for _ in range(n)]
        self.avail = [[0 for _ in range(m)] for _ in range(n)]
        for x, y, u, a in ls:
            self.used[x][y] = u
            self.avail[x][y] = a

    def solve_part_1(self):
        n, m = len(self.used), len(self.used[0])
        ans = 0
        for i in range(n):
            for j in range(m):
                for k in range(n):
                    for l in range(m):
                        if (i, j) != (k, l) and 0 < self.used[i][j] <= self.avail[k][l]:
                            ans += 1
        return ans

    def solve_part_2(self):
        n, m = len(self.used), len(self.used[0])
        block = [[0 for _ in range(m)] for _ in range(n)]
        M = 200
        for i in range(n):
            for j in range(m):
                if self.used[i][j] > M:
                    block[i][j] = 1
        ex, ey = -1, -1
        for i in range(n):
            for j in range(m):
                if self.used[i][j] == 0:
                    ex, ey = i, j
        fx, fy = n - 1, 0
        mp = {(fx, fy, ex, ey): 0}
        q = Queue()
        q.put((fx, fy, ex, ey))
        while q.qsize() > 0:
            fx, fy, ex, ey = q.get()
            if fx == 0 and fy == 0:
                return mp[fx, fy, ex, ey]
            for dx, dy in self.dirs:
                x, y = ex + dx, ey + dy
                if 0 <= x < n and 0 <= y < m and block[x][y] == 0:
                    if fx == x and fy == y:
                        tp = ex, ey, x, y
                    else:
                        tp = fx, fy, x, y
                    if tp not in mp.keys():
                        mp[tp] = mp[fx, fy, ex, ey] + 1
                        q.put(tp)


if __name__ == "__main__":
    src = get_data(Solver2016Day22.YEAR, Solver2016Day22.DAY)
    sol = Solver2016Day22(src)
    print(sol.solve_part_1())
    print(sol.solve_part_2())
