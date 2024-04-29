import requests

from utils import Solver


class Solver17D11(Solver):
    INPUT_URL = 'https://adventofcode.com/2017/day/11/input'

    def parse(self, src):
        return src.strip().split(',')

    dirs = {'n': (0, 1), 'ne': (1, 1), 'se': (1, 0), 's': (0, -1), 'sw': (-1, -1), 'nw': (-1, 0)}

    def _dis(self, x, y):
        if x * y >= 0:
            return max(abs(x), abs(y))
        else:
            return abs(x) + abs(y)

    def solve_part_1(self, src):
        ls = self.parse(src)

        x = y = 0
        for s in ls:
            x += self.dirs[s][0]
            y += self.dirs[s][1]
        return self._dis(x, y)

    def solve_part_2(self, src):
        ls = self.parse(src)
        ans = 0
        x = y = 0
        for s in ls:
            x += self.dirs[s][0]
            y += self.dirs[s][1]
            ans = max(ans, self._dis(x, y))
        return ans


if __name__ == "__main__":
    sol = Solver17D11()
    session = open('../.session').read().strip()
    cookies = {'session': session}

    src = requests.get(Solver17D11.INPUT_URL, cookies=cookies).text
    print(sol.solve_part_1(src))
    print(sol.solve_part_2(src))
