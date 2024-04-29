from collections import defaultdict

import requests

from utils import Solver, rotate


class Solver17D22(Solver):
    INPUT_URL = 'https://adventofcode.com/2017/day/22/input'
    dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]

    def parse(self, src):
        return src.strip().split()

    def solve_part_1(self, src):
        ls = self.parse(src)
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

    def solve_part_2(self, src):
        ls = self.parse(src)
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
    sol = Solver17D22()
    session = open('../.session').read().strip()
    cookies = {'session': session}

    src = requests.get(Solver17D22.INPUT_URL, cookies=cookies).text
    print(sol.solve_part_1(src))
    print(sol.solve_part_2(src))
