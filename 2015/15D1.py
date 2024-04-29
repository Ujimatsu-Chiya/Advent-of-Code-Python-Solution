import requests

from utils import Solver


class Solver15D1(Solver):
    INPUT_URL = 'https://adventofcode.com/2015/day/1/input'

    def parse(self, src):
        ls = src.strip().split()
        return ls

    def solve_part_1(self, src):
        ans = 0
        for s in self.parse(src):
            ans += s.count('(') - s.count(')')
        return ans

    def solve_part_2(self, src):
        ans = 0
        for s in self.parse(src):
            f = 0
            for i, ch in enumerate(s):
                f += 1 if ch == '(' else -1
                if f == -1:
                    ans += i + 1
                    break
        return ans


if __name__ == "__main__":
    sol = Solver15D1()
    session = open('../.session').read().strip()
    cookies = {'session': session}
    src = requests.get(Solver15D1.INPUT_URL, cookies=cookies).text
    print(sol.solve_part_1(src))
    print(sol.solve_part_2(src))
