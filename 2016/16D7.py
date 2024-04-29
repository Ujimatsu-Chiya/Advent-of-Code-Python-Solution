import re

import requests

from utils import Solver


class Solver16D7(Solver):
    INPUT_URL = 'https://adventofcode.com/2016/day/7/input'

    def parse(self, src):
        return src.strip().split()

    def _get(self, s):
        inside = re.findall(r'\[(.*?)\]', s)
        outside = re.sub(r'\[.*?\]', ' ', s).split()
        return inside, outside

    def solve_part_1(self, src):
        ls = self.parse(src)

        def ok(s):
            for i in range(len(s) - 3):
                if s[i] == s[i + 3] and s[i + 1] == s[i + 2] and s[i] != s[i + 1]:
                    return True
            return False

        ans = 0
        for s in ls:
            inside, outside = self._get(s)
            if all(not ok(s) for s in inside) and any(ok(s) for s in outside):
                ans += 1
        return ans

    def solve_part_2(self, src):
        ls = self.parse(src)
        ans = 0
        for s in ls:
            inside, outside = self._get(s)
            ok = False
            for s in inside:
                for i in range(len(s) - 2):
                    if s[i] == s[i + 2] and s[i] != s[i + 1]:
                        t = s[i + 1] + s[i] + s[i + 1]
                        ok |= any(t in w for w in outside)
            ans += ok
        return ans


if __name__ == "__main__":
    sol = Solver16D7()
    session = open('../.session').read().strip()
    cookies = {'session': session}
    src = requests.get(Solver16D7.INPUT_URL, cookies=cookies).text
    print(sol.solve_part_1(src))
    print(sol.solve_part_2(src))
