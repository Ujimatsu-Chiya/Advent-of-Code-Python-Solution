import re
from itertools import count

import requests

from utils import Solver


class Solver17D13(Solver):
    INPUT_URL = 'https://adventofcode.com/2017/day/13/input'

    def parse(self, src):
        pattern = r"(\d+): (\d+)"
        return [list(map(int, v)) for v in re.findall(pattern, src.strip())]

    def solve_part_1(self, src):
        a = self.parse(src)
        ans = 0
        for k, v in a:
            if k % (2 * (v - 1)) == 0:
                ans += k * v
        return ans

    def solve_part_2(self, src):
        a = self.parse(src)
        for t in count(0):
            if all((t + k) % (2 * (v - 1)) != 0 for k, v in a):
                return t


if __name__ == "__main__":
    sol = Solver17D13()
    session = open('../.session').read().strip()
    cookies = {'session': session}

    src = requests.get(Solver17D13.INPUT_URL, cookies=cookies).text
    print(sol.solve_part_1(src))
    print(sol.solve_part_2(src))
