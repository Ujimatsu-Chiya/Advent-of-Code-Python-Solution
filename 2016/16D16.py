import requests

from utils import Solver


class Solver16D16(Solver):
    INPUT_URL = 'https://adventofcode.com/2016/day/16/input'

    def parse(self, src):
        return src.strip()

    def solve_part_1(self, src):
        s = self.parse(src)
        M = 272
        while len(s) < M:
            s = s + "0" + "".join(['1' if ch == '0' else '0' for ch in s[::-1]])
        s = s[:M]
        while len(s) % 2 == 0:
            s = "".join(['1' if s[i] == s[i + 1] else '0' for i in range(0, len(s), 2)])
        return s

    def solve_part_2(self, src):
        s = self.parse(src)
        M = 35651584
        while len(s) < M:
            s = s + "0" + "".join(['1' if ch == '0' else '0' for ch in s[::-1]])
        s = s[:M]
        while len(s) % 2 == 0:
            s = "".join(['1' if s[i] == s[i + 1] else '0' for i in range(0, len(s), 2)])
        return s


if __name__ == "__main__":
    sol = Solver16D16()
    session = open('../.session').read().strip()
    cookies = {'session': session}
    src = requests.get(Solver16D16.INPUT_URL, cookies=cookies).text
    print(sol.solve_part_1(src))
    print(sol.solve_part_2(src))
