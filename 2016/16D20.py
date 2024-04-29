import re
import requests

from utils import Solver


class Solver16D20(Solver):
    INPUT_URL = 'https://adventofcode.com/2016/day/20/input'

    def parse(self, src):
        pat = re.compile(r"(\d+)-(\d+)")
        ls = []
        for tp in pat.findall(src.strip()):
            ls.append(list(map(int, tp)))
        return ls

    def solve_part_1(self, src):
        ls = sorted(self.parse(src))
        if ls[0][0] != 0:
            return 0
        pre = 0
        for x, y in ls:
            if x > pre + 1:
                return pre + 1
            pre = y
        return ls[-1][1] + 1

    def solve_part_2(self, src):
        ls = sorted(self.parse(src))
        a = []
        ans = 1 << 32
        for l, r in ls:
            if len(a) > 0 and l <= a[-1][1] + 1:
                a[-1][1] = max(a[-1][1], r)
            else:
                a.append([l, r])
        for l, r in a:
            ans -= r - l + 1
        return ans


if __name__ == "__main__":
    sol = Solver16D20()
    session = open('../.session').read().strip()
    cookies = {'session': session}
    src = requests.get(Solver16D20.INPUT_URL, cookies=cookies).text
    print(sol.solve_part_1(src))
    print(sol.solve_part_2(src))
