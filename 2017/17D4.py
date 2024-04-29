import requests

from utils import Solver


class Solver17D4(Solver):
    INPUT_URL = 'https://adventofcode.com/2017/day/4/input'

    def parse(self, src):
        return [s.split() for s in src.strip().split('\n')]

    def solve_part_1(self, src):
        ls = self.parse(src)
        return len([1 for v in ls if len(v) == len(set(v))])

    def solve_part_2(self, src):
        ls = self.parse(src)
        ans = 0
        for v in ls:
            v = list(map(lambda s: "".join((lambda x: (x.sort(), x)[1])(list(s))),v))
            if len(v) == len(set(v)):
                ans += 1
        return ans


if __name__ == "__main__":
    sol = Solver17D4()
    session = open('../.session').read().strip()
    cookies = {'session': session}

    src = requests.get(Solver17D4.INPUT_URL, cookies=cookies).text
    print(sol.solve_part_1(src))
    print(sol.solve_part_2(src))
