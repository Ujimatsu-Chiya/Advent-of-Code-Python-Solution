import re
import requests

from utils import Solver


class Solver15D6(Solver):
    INPUT_URL = 'https://adventofcode.com/2015/day/6/input'

    def parse(self, src):
        ls = re.findall("(toggle|turn on|turn off)\s(\d*),(\d*)\sthrough\s(\d*),(\d*)", src)
        return [[int(s) if s.isdigit() else s for s in v] for v in ls]

    def solve_part_1(self, src):
        M = 1000
        f = [[0 for _ in range(M)] for _ in range(M)]
        ls = self.parse(src)
        print(ls)
        for order, xa, ya, xb, yb in ls:
            for i in range(xa, xb + 1):
                for j in range(ya, yb + 1):
                    if order == "toggle":
                        f[i][j] ^= 1
                    elif order == "turn on":
                        f[i][j] = 1
                    else:
                        f[i][j] = 0
        return sum(sum(v) for v in f)

    def solve_part_2(self, src):
        M = 1000
        f = [[0 for _ in range(M)] for _ in range(M)]
        ls = self.parse(src)
        for order, xa, ya, xb, yb in ls:
            for i in range(xa, xb + 1):
                for j in range(ya, yb + 1):
                    if order == "toggle":
                        f[i][j] += 2
                    elif order == "turn on":
                        f[i][j] += 1
                    else:
                        f[i][j] = max(f[i][j] - 1, 0)
        return sum(sum(v) for v in f)


if __name__ == "__main__":
    sol = Solver15D6()
    session = open('../.session').read().strip()
    cookies = {'session': session}
    src = requests.get(Solver15D6.INPUT_URL, cookies=cookies).text
    print(sol.solve_part_1(src))
    print(sol.solve_part_2(src))
