import re

import requests

from utils import Solver


class Solver15D15(Solver):
    INPUT_URL = 'https://adventofcode.com/2015/day/15/input'

    def parse(self, src):
        pat = re.compile(
            r"(\w+): capacity (-?\d+), durability (-?\d+), flavor (-?\d+), texture (-?\d+), calories (\d+)")
        return [list(map(int, t[1:])) for t in pat.findall(src.strip())]

    def solve_part_1(self, src):
        ls = self.parse(src)
        ans = 0
        for i in range(100 + 1):
            for j in range(100 - i + 1):
                for k in range(100 - i - j + 1):
                    l = 100 - i - j - k
                    v = [max(i * ls[0][p] + j * ls[1][p] + k * ls[2][p] + l * ls[3][p], 0) for p in range(4)]
                    ans = max(ans, v[0] * v[1] * v[2] * v[3])
        return ans

    def solve_part_2(self, src):
        ls = self.parse(src)
        ans = 0
        for i in range(100 + 1):
            for j in range(100 - i + 1):
                for k in range(100 - i - j + 1):
                    l = 100 - i - j - k
                    v = [max(i * ls[0][p] + j * ls[1][p] + k * ls[2][p] + l * ls[3][p], 0) for p in range(5)]
                    if v[4] == 500:
                        ans = max(ans, v[0] * v[1] * v[2] * v[3])
        return ans


if __name__ == "__main__":
    sol = Solver15D15()
    session = open('../.session').read().strip()
    cookies = {'session': session}
    src = requests.get(Solver15D15.INPUT_URL, cookies=cookies).text
    print(sol.solve_part_1(src))
    print(sol.solve_part_2(src))
