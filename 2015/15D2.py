import requests

from utils import Solver


class Solver15D2(Solver):
    INPUT_URL = 'https://adventofcode.com/2015/day/2/input'

    def parse(self, src):
        return [list(map(int, s.split('x'))) for s in src.strip().split('\n')]

    def solve_part_1(self, src):
        ls = self.parse(src)
        ans = 0
        for u in ls:
            u.sort()
            ans += 3 * u[0] * u[1] + 2 * (u[0] + u[1]) * u[2]
        return ans

    def solve_part_2(self, src):
        ls = self.parse(src)
        ans = 0
        for u in ls:
            u.sort()
            ans += 2 * (u[0] + u[1]) + u[0] * u[1] * u[2]
        return ans


if __name__ == "__main__":
    sol = Solver15D2()
    session = open('../.session').read().strip()
    cookies = {'session': session}
    src = requests.get(Solver15D2.INPUT_URL, cookies=cookies).text
    print(sol.solve_part_1(src))
    print(sol.solve_part_2(src))
