from utils import Solver, get_data


class Solver2023Day10(Solver):
    YEAR = 2023
    DAY = 10
    dirs = {'|': {(1, 0), (-1, 0)}, '-': {(0, 1), (0, -1)},
            'L': {(0, 1), (-1, 0)}, 'J': {(-1, 0), (0, -1)},
            'F': {(0, 1), (1, 0)}, '7': {(1, 0), (0, -1)},
            '.': set()}
    all_dirs = dirs['|'] | dirs['-']

    def _resolve(self, mp):
        n, m = len(mp), len(mp[0])
        sx = sy = -1
        for i in range(n):
            for j in range(m):
                if mp[i][j] == 'S':
                    sx, sy = i, j
        st = set()
        for dx, dy in Solver2023Day10.all_dirs:
            x, y = sx + dx, sy + dy
            if 0 <= x < n and 0 <= y < m:
                for ex, ey in Solver2023Day10.dirs[mp[x][y]]:
                    tx, ty = x + ex, y + ey
                    if tx == sx and ty == sy:
                        st.add((-ex, -ey))
        for k, v in Solver2023Day10.dirs.items():
            if v == st:
                mp[sx][sy] = k
        return mp, sx, sy

    def _gen_path(self, mp, sx, sy):
        angle = 'LJF7'
        n, m = len(mp), len(mp[0])
        d = [[0 for _ in range(m)] for _ in range(n)]
        x, y = sx, sy
        path = []
        while True:
            ok = False
            for dx, dy in self.dirs[mp[x][y]]:
                tx, ty = x + dx, y + dy
                if d[tx][ty] == 0:
                    d[tx][ty] = 1
                    ok = True
                    x, y = tx, ty
                    if mp[x][y] in angle:
                        path.append((x, y))
                    break
            if not ok:
                break
        return path + [path[0]]

    def __init__(self, src):
        return [list(s) for s in src.strip().split('\n')]

    def solve_part_1(self):
        mp = self.parse(src)
        mp, sx, sy = self._resolve(mp)
        ls = self._gen_path(mp, sx, sy)
        ans = 0
        for i in range(len(ls) - 1):
            ans += abs(ls[i][0] - ls[i + 1][0]) + abs(ls[i][1] - ls[i + 1][1])
        return ans // 2

    def solve_part_2(self):
        mp = self.parse(src)
        mp, sx, sy = self._resolve(mp)
        ls = self._gen_path(mp, sx, sy)
        ans = premier = 0
        for i in range(len(ls) - 1):
            premier += abs(ls[i][0] - ls[i + 1][0]) + abs(ls[i][1] - ls[i + 1][1])
            ans += ls[i][0] * ls[i + 1][1] - ls[i][1] * ls[i + 1][0]
        return abs(ans) // 2 - premier // 2 + 1


if __name__ == "__main__":
    sol = Solver2023Day10()
    src = get_data(Solver2023Day10.YEAR, Solver2023Day10.DAY)
    print(sol.solve_part_1())
    print(sol.solve_part_2())
