import re

import requests

from utils import Solver


class Solver15D11(Solver):
    INPUT_URL = 'https://adventofcode.com/2015/day/11/input'

    def parse(self, src):
        return src.strip()

    def _solve(self, s):
        match = re.search(r'[iol]', s)
        if match:
            i = match.start()
            t = s[:i] + chr(ord(s[i]) + 1) + 'a' * (len(s) - i - 1)
            s = t
        while True:
            s = re.sub(r'([a-y])(z*)$', lambda x: chr(ord(x.group(1)) + 1) + len(x.group(2)) * "a", s)
            if ("i" in s or "o" in s or "l" in s) or \
                    (len(re.findall(r'([a-z])\1', s)) < 2) or \
                    (len([1 for x, y, z in zip(s, s[1:], s[2:])
                          if ord(z) - ord(y) == 1 and ord(y) - ord(x) == 1]) == 0):
                continue
            return s

    def solve_part_1(self, src):
        s = self.parse(src)
        return self._solve(s)

    def solve_part_2(self, src):
        return self._solve(self.solve_part_1(src))


if __name__ == "__main__":
    sol = Solver15D11()
    session = open('../.session').read().strip()
    cookies = {'session': session}
    src = requests.get(Solver15D11.INPUT_URL, cookies=cookies).text
    print(sol.solve_part_1(src))
    print(sol.solve_part_2(src))
