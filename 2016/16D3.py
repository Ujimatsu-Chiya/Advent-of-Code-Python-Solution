import requests

from utils import Solver


class Solver16D3(Solver):
    INPUT_URL = 'https://adventofcode.com/2016/day/3/input'

    def parse(self, src):
        return [list(map(int, s.split())) for s in src.strip().split('\n')]

    def solve_part_1(self, src):
        ls = self.parse(src)
        ans = 0
        for v in ls:
            x, y, z = sorted(v)
            if x + y > z:
                ans += 1
        return ans

    def solve_part_2(self, src):
        ls = self.parse(src)
        ans = 0
        for i in range(0, len(ls), 3):
            for j in range(3):
                x, y, z = sorted([ls[i + k][j] for k in range(3)])
                if x + y > z:
                    ans += 1
        return ans


if __name__ == "__main__":
    sol = Solver16D3()
    session = open('../.session').read().strip()
    cookies = {'session': session}
    src = requests.get(Solver16D3.INPUT_URL, cookies=cookies).text
    print(sol.solve_part_1(src))
    print(sol.solve_part_2(src))
