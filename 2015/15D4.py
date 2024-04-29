import hashlib
from itertools import count

import requests

from utils import Solver


class Solver15D4(Solver):
    INPUT_URL = 'https://adventofcode.com/2015/day/4/input'

    def parse(self, src):
        return src.strip()

    def _solve(self, s, prefix):
        for i in count(1):
            md5 = hashlib.md5((s + str(i)).encode())
            if md5.hexdigest().startswith(prefix):
                return i

    def solve_part_1(self, src):
        s = self.parse(src)
        return self._solve(s, '0' * 5)

    def solve_part_2(self, src):
        s = self.parse(src)
        return self._solve(s, '0' * 6)


if __name__ == "__main__":
    sol = Solver15D4()
    session = open('../.session').read().strip()
    cookies = {'session': session}
    src = requests.get(Solver15D4.INPUT_URL, cookies=cookies).text
    print(sol.solve_part_1(src))
    print(sol.solve_part_2(src))
