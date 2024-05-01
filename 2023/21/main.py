from queue import Queue

from utils import Solver, get_data


class Solver2023Day21(Solver):
    YEAR = 2023
    DAY = 21

    def parse(self, src):
        return src.strip().split('\n')

    def solve_part_1(self, src):
        dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        mq = self.parse(src)
        mp = []
        for i in range(1):
            mp += mq

        M = 64
        n, m = len(mp), len(mp[0])
        sx, sy = -1, -1
        for i in range(n):
            for j in range(m):
                if mp[i][j] == 'S':
                    sx, sy = i, j
        d = [[-1 for _ in range(m)] for _ in range(n)]
        q = Queue()
        d[sx][sy] = 0
        q.put((sx, sy))
        while q.qsize() > 0:
            sx, sy = q.get()
            for dx, dy in dirs:
                x, y = sx + dx, sy + dy
                if 0 <= x < n and 0 <= y < m and mp[x][y] != '#' and d[x][y] == -1:
                    d[x][y] = d[sx][sy] + 1
                    q.put((x, y))
        ans = 0
        for i in range(n):
            for j in range(m):
                if d[i][j] != -1 and d[i][j] <= M and (M - d[i][j]) % 2 == 0:
                    ans += 1
        return ans

    def solve_part_2(self, src):
        pass


if __name__ == "__main__":
    sol = Solver2023Day21()
    src = get_data(Solver2023Day21.YEAR, Solver2023Day21.DAY)
    print(sol.solve_part_1(src))
    print(sol.solve_part_2(src))
