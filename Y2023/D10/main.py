from itertools import pairwise

from utils import Solver, get_data


class Solver2023Day10(Solver):
    YEAR = 2023
    DAY = 10
    dirs = {'|': {(1, 0), (-1, 0)}, '-': {(0, 1), (0, -1)},
            'L': {(0, 1), (-1, 0)}, 'J': {(-1, 0), (0, -1)},
            'F': {(0, 1), (1, 0)}, '7': {(1, 0), (0, -1)},
            '.': set()}
    all_dirs = dirs['|'] | dirs['-']

    def run(self):
        n, m = len(self.mp), len(self.mp[0])
        sx = sy = -1
        for i in range(n):
            for j in range(m):
                if self.mp[i][j] == 'S':
                    sx, sy = i, j
        st = set()
        for dx, dy in Solver2023Day10.all_dirs:
            x, y = sx + dx, sy + dy
            if 0 <= x < n and 0 <= y < m:
                for ex, ey in Solver2023Day10.dirs[self.mp[x][y]]:
                    tx, ty = x + ex, y + ey
                    if tx == sx and ty == sy:
                        st.add((-ex, -ey))
        for k, v in Solver2023Day10.dirs.items():
            if v == st:
                self.mp[sx][sy] = k

        angle = 'LJF7'
        d = [[0 for _ in range(m)] for _ in range(n)]
        x, y = sx, sy
        path = []
        while True:
            ok = False
            for dx, dy in self.dirs[self.mp[x][y]]:
                tx, ty = x + dx, y + dy
                if d[tx][ty] == 0:
                    d[tx][ty] = 1
                    ok = True
                    x, y = tx, ty
                    if self.mp[x][y] in angle:
                        path.append((x, y))
                    break
            if not ok:
                break
        premier = 0
        tmp = 0
        for pa, pb in pairwise(path + [path[0]]):
            premier += abs(pa[0] - pb[0]) + abs(pa[1] - pb[1])
            tmp += pa[0] * pb[1] - pa[1] * pb[0]
        self.ans1 = premier // 2
        self.ans2 = abs(tmp) // 2 - premier // 2 + 1

    def __init__(self, src):
        self.mp = [list(s) for s in src.strip().split('\n')]
        self.ans1 = self.ans2 = None

    def solve_part_1(self):
        return self.ans1

    def solve_part_2(self):
        return self.ans2


if __name__ == "__main__":
    src = get_data(Solver2023Day10.YEAR, Solver2023Day10.DAY)
    sol = Solver2023Day10(src)
    sol.run()
    print(sol.solve_part_1())
    print(sol.solve_part_2())
