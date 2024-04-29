import re
from collections import Counter, defaultdict

import numpy as np
import requests

from utils import Solver


class Solver18D5(Solver):
    INPUT_URL = 'https://adventofcode.com/2018/day/5/input'

    def parse(self, src):
        return src.strip()

    def _solve(self, ls):
        st = []
        M = 32
        for x in ls:
            if len(st) > 0 and st[-1] == x ^ M:
                st.pop()
            else:
                st.append(x)
        return len(st)

    def solve_part_1(self, src):
        ls = [ord(ch) for ch in self.parse(src)]
        return self._solve(ls)

    def solve_part_2(self, src):
        s = self.parse(src)
        char_set = set(s.lower())
        ans = min(self._solve([ord(ch) for ch in s.replace(ch, "").replace(ch.upper(), "")]) for ch in char_set)
        return ans


if __name__ == "__main__":
    sol = Solver18D5()
    session = open('../.session').read().strip()
    cookies = {'session': session}

    src = requests.get(Solver18D5.INPUT_URL, cookies=cookies).text
    print(sol.solve_part_1(src))
    print(sol.solve_part_2(src))
