import re

import requests

from utils import Solver


class Solver17D9(Solver):
    INPUT_URL = 'https://adventofcode.com/2017/day/9/input'

    def parse(self, src):
        return src.strip()

    def solve_part_1(self, src):
        s = self.parse(src)
        s = re.sub(r"!.", "", s)
        s = re.sub(r"<.*?>", "", s)
        ans = cnt = 0
        for ch in s:
            if ch == '{':
                cnt += 1
            elif ch == '}':
                ans += cnt
                cnt -= 1
        return ans

    def solve_part_2(self, src):
        s = self.parse(src)
        s = re.sub(r"!.", "", s)
        t = re.sub(r"<.*?>", "<>", s)
        return len(s) - len(t)


if __name__ == "__main__":
    sol = Solver17D9()
    session = open('../.session').read().strip()
    cookies = {'session': session}

    src = requests.get(Solver17D9.INPUT_URL, cookies=cookies).text
    print(sol.solve_part_1(src))
    print(sol.solve_part_2(src))
