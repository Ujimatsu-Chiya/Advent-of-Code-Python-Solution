import requests
from collections import defaultdict

from utils import Solver


class Solver23D3(Solver):
    INPUT_URL = 'https://adventofcode.com/2023/day/3/input'
    def _gen_pos(self, i, j, k, n, m):
        ps1 = list(zip([i - 1] * (k - j + 2), range(j - 1, k + 1)))
        ps2 = list(zip([i + 1] * (k - j + 2), range(j - 1, k + 1)))
        ps3 = [(i, j - 1), (i, k)]
        return [(x, y) for x, y in ps1 + ps2 + ps3 if 0 <= x < n and 0 <= y < m]

    def parse(self, src):
        return src.strip().split('\n')

    def solve_part_1(self, src):
        def ok(mp, i, j, k):
            return any(
                not mp[x][y].isdigit() and mp[x][y] != '.' for x, y in self._gen_pos(i, j, k, len(mp), len(mp[0])))

        ans = 0
        mp = self.parse(src)
        n, m = len(mp), len(mp[0])
        for i in range(n):
            j = 0
            while j < m:
                if mp[i][j].isdigit():
                    k = j
                    while k < m and mp[i][k].isdigit():
                        k += 1
                    if ok(mp, i, j, k):
                        ans += int(mp[i][j:k])
                    j = k
                else:
                    j += 1
        return ans

    def solve_part_2(self, src):
        mp = self.parse(src)
        n, m = len(mp), len(mp[0])
        mq = defaultdict(list)
        for i in range(n):
            j = 0
            while j < m:
                if mp[i][j].isdigit():
                    k = j
                    while k < m and mp[i][k].isdigit():
                        k += 1
                    for x, y in self._gen_pos(i, j, k, len(mp), len(mp[0])):
                        if mp[x][y] == '*':
                            mq[x, y].append(int(mp[i][j:k]))
                    j = k
                else:
                    j += 1
        ans = 0
        for v in mq.values():
            if len(v) == 2:
                ans += v[0] * v[1]
        return ans


if __name__ == "__main__":
    sol = Solver23D3()
    session = open('../.session').read().strip()
    cookies = {'session': session}
    src = requests.get(Solver23D3.INPUT_URL, cookies=cookies).text
    print(sol.solve_part_1(src))
    print(sol.solve_part_2(src))
