import requests

from utils import Solver


class Solver16D18(Solver):
    INPUT_URL = 'https://adventofcode.com/2016/day/18/input'

    def parse(self, src):
        return [int(ch == '^') for ch in src.strip()]

    def solve_part_1(self, src):
        ls = self.parse(src)
        m = len(ls)
        n = 40
        ls = [0] + ls + [0]
        ans = m - sum(ls)
        for _ in range(n - 1):
            ls = [0] + [int(sum(ls[i - 1:i + 2]) == 2 and ls[i] == 1 or
                            sum(ls[i - 1:i + 2]) == 1 and ls[i] == 0) for i in range(1, m + 1)] + [0]
            ans += m - sum(ls)
        return ans

    def solve_part_2(self, src):
        ls = self.parse(src)
        m = len(ls)
        n = 400000
        ls = [0] + ls + [0]
        ans = m - sum(ls)
        for _ in range(n - 1):
            ls = [0] + [int(sum(ls[i - 1:i + 2]) == 2 and ls[i] == 1 or
                            sum(ls[i - 1:i + 2]) == 1 and ls[i] == 0) for i in range(1, m + 1)] + [0]
            ans += m - sum(ls)
        return ans


if __name__ == "__main__":
    sol = Solver16D18()
    session = open('../.session').read().strip()
    cookies = {'session': session}
    src = requests.get(Solver16D18.INPUT_URL, cookies=cookies).text
    print(sol.solve_part_1(src))
    print(sol.solve_part_2(src))
