import requests

from utils import Solver


class Solver17D2(Solver):
    INPUT_URL = 'https://adventofcode.com/2017/day/2/input'

    def parse(self, src):
        return [list(map(int,s.split())) for s in src.strip().split('\n')]

    def solve_part_1(self, src):
        a = self.parse(src)
        return sum(max(v) - min(v) for v in a)

    def solve_part_2(self, src):
        a = self.parse(src)
        ans = 0
        for v in a:
            for x in v:
                for y in v:
                    if y > x and y % x == 0:
                        ans += y // x
        return ans


if __name__ == "__main__":
    sol = Solver17D2()
    session = open('../.session').read().strip()
    cookies = {'session': session}

    src = requests.get(Solver17D2.INPUT_URL, cookies=cookies).text
    print(sol.solve_part_1(src))
    print(sol.solve_part_2(src))
