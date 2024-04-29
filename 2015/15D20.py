import requests

from utils import Solver, divisors_sigma
from itertools import count


class Solver15D20(Solver):
    INPUT_URL = 'https://adventofcode.com/2015/day/20/input'

    def parse(self, src):
        return int(src.strip())
        pass

    def solve_part_1(self, src):
        n = self.parse(src)
        for i in count(1):
            if divisors_sigma(i) * 10 >= n:
                return i

    def solve_part_2(self, src):
        n = self.parse(src)
        M = 50
        for i in count(1):
            s = 0
            for j in range(1, M + 1):
                if i % j == 0:
                    s += i // j
            if s * 11 >= n:
                return i


if __name__ == "__main__":
    sol = Solver15D20()
    session = open('../.session').read().strip()
    cookies = {'session': session}
    src = requests.get(Solver15D20.INPUT_URL, cookies=cookies).text
    print(sol.solve_part_1(src))
    print(sol.solve_part_2(src))
