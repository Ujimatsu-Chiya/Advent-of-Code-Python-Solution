from collections import defaultdict

from utils import Solver, get_data


class Solver2017Day22(Solver):
    YEAR = 2017
    DAY = 22
    dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]

    def __init__(self, src):
        self.ls = src.strip().split()

    def solve_part_1(self):
        ls = self.ls.copy()
        M = 10000
        mp = defaultdict(int)
        n, m = len(ls), len(ls[0])
        x, y, d = n // 2, m // 2, 0
        for i in range(n):
            for j in range(m):
                if ls[i][j] == '#':
                    mp[i, j] = 1
        cnt = 0
        for i in range(M):
            if mp[x, y]:
                d = (d + 1) % 4
            else:
                d = (d - 1) % 4
            mp[x, y] ^= 1
            if mp[x, y]:
                cnt += 1
            x += self.dirs[d][0]
            y += self.dirs[d][1]

        return cnt

    def solve_part_2(self):
        ls = self.ls.copy()
        M = 10 ** 7
        mp = defaultdict(int)
        n, m = len(ls), len(ls[0])
        x, y, d = n // 2, m // 2, 0
        for i in range(n):
            for j in range(m):
                if ls[i][j] == '#':
                    mp[i, j] = 2
        cnt = 0
        for i in range(M):
            if mp[x, y] == 0:
                d = (d - 1) & 3
            elif mp[x, y] == 2:
                d = (d + 1) & 3
            elif mp[x, y] == 3:
                d ^= 2
            mp[x, y] = (mp[x, y] + 1) & 3
            if mp[x, y] == 2:
                cnt += 1
            x += self.dirs[d][0]
            y += self.dirs[d][1]

        return cnt


if __name__ == "__main__":
    src = get_data(Solver2017Day22.YEAR, Solver2017Day22.DAY)
    sol = Solver2017Day22(src)
    print(sol.solve_part_1())
    print(sol.solve_part_2())
