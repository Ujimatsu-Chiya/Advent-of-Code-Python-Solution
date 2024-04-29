import requests

from utils import Solver


class Solver17D1(Solver):
    INPUT_URL = 'https://adventofcode.com/2017/day/1/input'

    def parse(self, src):
        return src.strip()

    def solve_part_1(self, src):
        s = self.parse(src)
        return sum(int(s[i]) for i in range(len(s)) if s[i] == s[(i + 1) % len(s)])

    def solve_part_2(self, src):
        s = self.parse(src)
        return sum(int(s[i]) * 2 for i in range(len(s) // 2) if s[i] == s[i+len(s) // 2])


if __name__ == "__main__":
    sol = Solver17D1()
    session = open('../.session').read().strip()
    cookies = {'session': session}

    src = requests.get(Solver17D1.INPUT_URL, cookies=cookies).text
    print(sol.solve_part_1(src))
    print(sol.solve_part_2(src))
