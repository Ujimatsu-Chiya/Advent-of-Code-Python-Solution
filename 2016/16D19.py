import requests

from utils import Solver


class Solver16D19(Solver):
    INPUT_URL = 'https://adventofcode.com/2016/day/19/input'

    def parse(self, src):
        return int(src.strip())

    def solve_part_1(self, src):
        # https://oeis.org/A006257
        n = self.parse(src)

        def cal(n):
            if n == 1:
                return 1
            elif n % 2 == 0:
                return cal(n // 2) * 2 - 1
            else:
                return cal(n // 2) * 2 + 1

        return cal(n)

    def solve_part_2(self, src):
        # https://oeis.org/A334473
        n = self.parse(src)
        k = 0
        while 3 ** (k + 1) <= n:
            k += 1
        b = n - 3 ** k
        if b == 0:
            return n
        elif 3 ** k + b <= 2 * 3 ** k:
            return b
        else:
            return 2 * b - 3 ** k


if __name__ == "__main__":
    sol = Solver16D19()
    session = open('../.session').read().strip()
    cookies = {'session': session}
    src = requests.get(Solver16D19.INPUT_URL, cookies=cookies).text
    print(sol.solve_part_1(src))
    print(sol.solve_part_2(src))
