from collections import defaultdict
from itertools import count
from queue import Queue

import requests

from utils import Solver


class Solver17D19(Solver):
    INPUT_URL = 'https://adventofcode.com/2017/day/19/input'

    def parse(self, src):
        return src.rstrip('\n').split('\n')

    dirs = [[-1, 0], [1, 0], [0, 1], [0, -1]]

    def solve_part_1(self, src):
        mp = self.parse(src)
        n, m = len(mp), len(mp[0])

        def in_path(x, y):
            return 0 <= x < n and 0 <= y < m and mp[x][y] != ' '

        x, y, d = 0, mp[0].index('|'), 0
        ans = ''
        while True:
            if not in_path(x + self.dirs[d][0], y + self.dirs[d][1]):
                d ^= 1
            x += self.dirs[d][0]
            y += self.dirs[d][1]
            while in_path(x, y) and mp[x][y] != '+':
                if mp[x][y].isalpha():
                    ans += mp[x][y]
                x += self.dirs[d][0]
                y += self.dirs[d][1]
            if mp[x][y] == '+':
                d ^= 2
            else:
                break
        return ans

    def solve_part_2(self, src):
        mp = self.parse(src)
        n, m = len(mp), len(mp[0])

        def in_path(x, y):
            return 0 <= x < n and 0 <= y < m and mp[x][y] != ' '

        return sum(1 + all(in_path(i + dx, j + dy) for dx, dy in self.dirs) for j in range(m) for i in range(n) if
                   in_path(i, j))


if __name__ == "__main__":
    sol = Solver17D19()
    session = open('../.session').read().strip()
    cookies = {'session': session}

    src = requests.get(Solver17D19.INPUT_URL, cookies=cookies).text
    print(sol.solve_part_1(src))
    print(sol.solve_part_2(src))
