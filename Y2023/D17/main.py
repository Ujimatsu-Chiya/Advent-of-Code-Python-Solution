from queue import PriorityQueue

from utils import Solver, get_data

dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]


class Solver2023Day17(Solver):
    YEAR = 2023
    DAY = 17

    def __init__(self, src):
        return src.strip().split()

    def solve_part_1(self):
        ls = self.parse(src)
        a = [[int(ch) for ch in s] for s in ls]
        n, m = len(ls), len(ls[0])
        inf = n * m * 10
        dis = [[[[inf for _ in range(3)] for _ in range(4)] for _ in range(m)] for _ in range(n)]
        q = PriorityQueue()
        q.put((0, 0, 0, 3, 0))
        q.put((0, 0, 0, 2, 0))
        while q.qsize() > 0:
            val, x, y, d, c = q.get()
            if dis[x][y][d][c] != inf:
                continue
            dis[x][y][d][c] = val
            for i in range(4):
                tx, ty = x + dirs[i][0], y + dirs[i][1]
                if not (0 <= tx < n and 0 <= ty < m) or abs(i - d) == 2:
                    continue
                tc = c + 1 if i == d else 0
                if tc < 3 and dis[tx][ty][i][tc] == inf:
                    q.put((val + a[tx][ty], tx, ty, i, tc))
        ans = min(dis[-1][-1][i][j] for i in range(4) for j in range(3))
        return ans

    def solve_part_2(self):
        ls = self.parse(src)
        a = [[int(ch) for ch in s] for s in ls]
        n, m = len(ls), len(ls[0])
        inf = n * m * 10
        dis = [[[[inf for _ in range(7)] for _ in range(4)] for _ in range(m)] for _ in range(n)]
        q = PriorityQueue()
        q.put((0, 0, 0, 2, 0))
        q.put((0, 0, 0, 3, 0))
        while q.qsize() > 0:
            val, x, y, d, c = q.get()
            if dis[x][y][d][c] != inf:
                continue
            dis[x][y][d][c] = val
            tx, ty = x + dirs[d][0], y + dirs[d][1]
            tc = c + 1
            if 0 <= tx < n and 0 <= ty < m and tc < 7 and dis[tx][ty][d][tc] == inf:
                q.put((val + a[tx][ty], tx, ty, d, tc))
            for i in range(4):
                tx, ty = x + dirs[i][0] * 4, y + dirs[i][1] * 4
                if (i - d) % 2 == 0 or not (0 <= tx < n and 0 <= ty < m) or dis[tx][ty][i][0] != inf:
                    continue
                w = 0
                for k in range(1, 4 + 1):
                    w += a[x + dirs[i][0] * k][y + dirs[i][1] * k]
                q.put((val + w, tx, ty, i, 0))

        ans = min(dis[-1][-1][i][j] for i in range(4) for j in range(7))
        return ans


if __name__ == "__main__":
    sol = Solver2023Day17()
    src = get_data(Solver2023Day17.YEAR, Solver2023Day17.DAY)
    print(sol.solve_part_1())
    print(sol.solve_part_2())
