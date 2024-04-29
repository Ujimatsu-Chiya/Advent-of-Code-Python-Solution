import requests

from utils import Solver


class Solver15D10(Solver):
    INPUT_URL = 'https://adventofcode.com/2015/day/10/input'

    def parse(self, src):
        return src.strip()

    def _solve(self, s):
        ls = []
        i = 0
        while i < len(s):
            j = i
            while j < len(s) and s[i] == s[j]:
                j += 1
            ls += [str(j - i), s[i]]
            i = j
        return ''.join(ls)

    def solve_part_1(self, src):
        s = self.parse(src)
        for i in range(40):
            s = self._solve(s)
        return len(s)

    def solve_part_2(self, src):
        s = self.parse(src)
        for i in range(50):
            s = self._solve(s)
        return len(s)


if __name__ == "__main__":
    sol = Solver15D10()
    session = open('../.session').read().strip()
    cookies = {'session': session}
    src = requests.get(Solver15D10.INPUT_URL, cookies=cookies).text
    print(sol.solve_part_1(src))
    print(sol.solve_part_2(src))
