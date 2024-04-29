import requests

from utils import Solver


class Solver23D11(Solver):
    INPUT_URL = 'https://adventofcode.com/2023/day/11/input'

    def parse(self, src):
        return src.strip().split('\n')

    def solve_part_1(self, src):
        mp = self.parse(src)
        n, m = len(mp), len(mp[0])
        cx = [0 for _ in range(n)]
        cy = [0 for _ in range(m)]
        for i in range(n):
            for j in range(m):
                if mp[i][j] == '#':
                    cx[i] += 1
                    cy[j] += 1

        kx = [int(w == 0) for w in cx]
        ky = [int(w == 0) for w in cy]
        for i in range(1, n):
            kx[i] += kx[i - 1]
        for j in range(1, m):
            ky[j] += ky[j - 1]
        ls = []
        for i in range(n):
            for j in range(m):
                if mp[i][j] == '#':
                    ls.append((i + kx[i], j + ky[j]))
        ans = 0
        for i in range(len(ls)):
            for j in range(i + 1, len(ls)):
                ans += abs(ls[i][0] - ls[j][0]) + abs(ls[i][1] - ls[j][1])
        return ans

    def solve_part_2(self, src):
        M = 1000000
        mp = self.parse(src)
        n, m = len(mp), len(mp[0])
        cx = [0 for _ in range(n)]
        cy = [0 for _ in range(m)]
        for i in range(n):
            for j in range(m):
                if mp[i][j] == '#':
                    cx[i] += 1
                    cy[j] += 1

        kx = [int(w == 0) for w in cx]
        ky = [int(w == 0) for w in cy]
        for i in range(1, n):
            kx[i] += kx[i - 1]
        for j in range(1, m):
            ky[j] += ky[j - 1]
        ls = []
        for i in range(n):
            for j in range(m):
                if mp[i][j] == '#':
                    ls.append((i + kx[i] * (M - 1), j + ky[j] * (M - 1)))
        ans = 0
        for i in range(len(ls)):
            for j in range(i + 1, len(ls)):
                ans += abs(ls[i][0] - ls[j][0]) + abs(ls[i][1] - ls[j][1])
        return ans


if __name__ == "__main__":
    sol = Solver23D11()
    session = open('../.session').read().strip()
    cookies = {'session': session}
    src = requests.get(Solver23D11.INPUT_URL, cookies=cookies).text
    print(sol.solve_part_1(src))
    print(sol.solve_part_2(src))
