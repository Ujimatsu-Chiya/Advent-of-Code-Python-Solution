import requests

from utils import Solver


class Solver15D8(Solver):
    INPUT_URL = 'https://adventofcode.com/2015/day/8/input'

    def parse(self, src):
        return src.strip().split('\n')

    def solve_part_1(self, src):
        ls = self.parse(src)
        ans = 0
        for s in ls:
            ans += len(s) - len(eval(s))
        return ans

    def solve_part_2(self, src):
        ls = self.parse(src)
        ans = 0
        lt = str(ls).strip('[]').replace(r'"', r'\"').split(', ')
        for s, t in zip(ls, lt):
            ans += len(t) - len(s)
        return ans


if __name__ == "__main__":
    sol = Solver15D8()
    session = open('../.session').read().strip()
    cookies = {'session': session}
    src = requests.get(Solver15D8.INPUT_URL, cookies=cookies).text
    print(sol.solve_part_1(src))
    print(sol.solve_part_2(src))
