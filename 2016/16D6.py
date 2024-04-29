from collections import Counter

import requests

from utils import Solver


class Solver16D6(Solver):
    INPUT_URL = 'https://adventofcode.com/2016/day/6/input'

    def parse(self, src):
        return src.strip().split()

    def solve_part_1(self, src):
        ls = self.parse(src)
        n, m = len(ls), len(ls[0])
        ans = ''
        for j in range(m):
            c = Counter(ls[i][j] for i in range(n))
            ch = max(c, key=c.get)
            ans += ch
        return ans

    def solve_part_2(self, src):
        ls = self.parse(src)
        n, m = len(ls), len(ls[0])
        ans = ''
        for j in range(m):
            c = Counter(ls[i][j] for i in range(n))
            ch = min(c, key=c.get)
            ans += ch
        return ans


if __name__ == "__main__":
    sol = Solver16D6()
    session = open('../.session').read().strip()
    cookies = {'session': session}
    src = requests.get(Solver16D6.INPUT_URL, cookies=cookies).text
    print(sol.solve_part_1(src))
    print(sol.solve_part_2(src))
