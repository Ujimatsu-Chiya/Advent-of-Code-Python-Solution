import operator
from functools import reduce
from queue import Queue

import requests

from utils import Solver


class Solver17D14(Solver):
    INPUT_URL = 'https://adventofcode.com/2017/day/14/input'

    def parse(self, src):
        return src.strip()

    def _solve(self, s):
        a = [ord(x) for x in s]
        a = (a + [17, 31, 73, 47, 23]) * 64
        M = 256
        b = list(range(M))
        p = 0
        for skip_size, x in enumerate(a):
            if p + x <= M:
                l, m, r = b[:p], b[p:p + x], b[p + x:]
                b = l + list(reversed(m)) + r
            else:
                rev = list(reversed(b[p:] + b[:x - (M - p)]))
                rest = b[x - (M - p):p]
                b = rev[- (x - (M - p)):] + rest + rev[:-(x - (M - p))]
            p = (p + x + skip_size) % M
            skip_size += 1
        t = [reduce(operator.xor, b[i:i + 16]) for i in range(0, len(b), 16)]
        return "".join("{:02x}".format(x) for x in t)

    def solve_part_1(self, src):
        s = self.parse(src)
        ans = 0
        for i in range(128):
            h = self._solve(s + '-' + str(i))
            ans += int(h, 16).bit_count()
        return ans

    def solve_part_2(self, src):
        s = self.parse(src)
        ls = []
        for i in range(128):
            h = self._solve(s + '-' + str(i))
            ls.append("{:0128b}".format(int(h, 16)))
        n, m = len(ls), len(ls[0])
        dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        q = Queue()
        d = [[0 for _ in range(n)] for _ in range(n)]
        cnt = 0
        for i in range(n):
            for j in range(m):
                if ls[i][j] == '1' and d[i][j] == 0:
                    cnt += 1
                    q.put((i, j))
                    d[i][j] = 1
                    while q.qsize() > 0:
                        sx, sy = q.get()
                        for dx, dy in dirs:
                            x, y = sx + dx, sy + dy
                            if 0 <= x < n and 0 <= y < m and ls[x][y] == '1' and d[x][y] == 0:
                                q.put((x, y))
                                d[x][y] = 1
                                q.put((x, y))
        return cnt


if __name__ == "__main__":
    sol = Solver17D14()
    session = open('../.session').read().strip()
    cookies = {'session': session}

    src = requests.get(Solver17D14.INPUT_URL, cookies=cookies).text
    print(sol.solve_part_1(src))
    print(sol.solve_part_2(src))
