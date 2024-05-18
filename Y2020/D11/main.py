from utils import Solver, get_data
from itertools import chain,count

class Solver2020Day11(Solver):
    YEAR = 2020
    DAY = 11
    dirs = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]

    def __init__(self, src):
        ls = src.strip().split()
        self.a = [[2 if ls[i][j] == '.' else 0 for j in range(len(ls[0]))] for i in range(len(ls))]

    def _run(self, a, g, M):
        def trans(p):
            if a[p] == 2:
                return 2
            cnt = sum(a[x] == 1 for x in g[p])
            return a[p] ^ 1 if a[p] == 0 and cnt == 0 or a[p] == 1 and cnt >= M else a[p]

        while True:
            b = [trans(p) for p in range(len(a))]
            if b == a:
                return b
            a = b

    def solve_part_1(self):
        n, m = len(self.a), len(self.a[0])
        pos_2_index = [[i * m + j for j in range(m)] for i in range(n)]
        g = [[] for _ in range(n * m)]
        for i in range(n):
            for j in range(m):
                if self.a[i][j] == 0:
                    for dx, dy in self.dirs:
                        x, y = i + dx, j + dy
                        if 0 <= x < n and 0 <= y < m and self.a[x][y] == 0:
                            g[pos_2_index[i][j]].append(pos_2_index[x][y])
        a = list(chain.from_iterable(self.a))
        b = self._run(a, g, 4)
        return b.count(1)

    def solve_part_2(self):
        n, m = len(self.a), len(self.a[0])
        pos_2_index = [[i * m + j for j in range(m)] for i in range(n)]
        g = [[] for _ in range(n * m)]
        for i in range(n):
            for j in range(m):
                if self.a[i][j] == 0:
                    for dx, dy in self.dirs:
                        for k in count(1):
                            x, y = i + dx * k, j + dy * k
                            if not(0 <= x < n and 0 <= y < m):
                                break
                            if self.a[x][y] == 0:
                                g[pos_2_index[i][j]].append(pos_2_index[x][y])
                                break
        a = list(chain.from_iterable(self.a))
        b = self._run(a, g, 5)
        return b.count(1)


if __name__ == "__main__":
    src = get_data(Solver2020Day11.YEAR, Solver2020Day11.DAY)
    sol = Solver2020Day11(src)
    print(sol.solve_part_1())
    print(sol.solve_part_2())
