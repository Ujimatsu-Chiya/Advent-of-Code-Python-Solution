import re
import requests

from utils import Solver


class Solver23D1(Solver):
    INPUT_URL = 'https://adventofcode.com/2023/day/1/input'

    def parse(self, src):
        ls = src.strip().split()
        return ls

    def solve_part_1(self, src):
        inputs = self.parse(src)

        def cal(s):
            d = [ch for ch in s if ch.isdigit()]
            return int(d[0] + d[-1])

        ans = 0
        for s in inputs:
            ans += cal(s)
        return ans

    def solve_part_2(self, src):
        inputs = self.parse(src)
        ls = "one two three four five six seven eight nine".split()
        pat = "(?=(" + "|".join(ls) + "|\\d))"

        def cal(s):
            d = list(map(lambda t: str(ls.index(t) + 1) if t in ls else t, re.findall(pat, s)))
            return int(d[0] + d[-1])

        ans = 0
        for s in inputs:
            ans += cal(s)
        return ans


if __name__ == "__main__":
    sol = Solver23D1()
    session = open('../.session').read().strip()
    cookies = {'session': session}
    src = requests.get(Solver23D1.INPUT_URL, cookies=cookies).text
    print(sol.solve_part_1(src))
    print(sol.solve_part_2(src))
