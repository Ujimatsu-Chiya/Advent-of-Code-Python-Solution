from collections import defaultdict

import requests

from utils import Solver


class Solver17D8(Solver):
    INPUT_URL = 'https://adventofcode.com/2017/day/8/input'

    def parse(self, src):
        ls = []
        for s in src.strip().split('\n'):
            l, r = s.split(' if ')
            tp = l.strip().split()
            if tp[1] == "inc":
                ls.append([tp[0], int(tp[2]), r.strip()])
            else:
                ls.append([tp[0], -int(tp[2]), r.strip()])
        return ls

    def solve_part_1(self, src):
        ls = self.parse(src)
        mp = defaultdict(int)
        for reg, delta, cond in ls:
            if eval(cond, mp):
                mp[reg] += delta
        return max(x for x in mp.values() if isinstance(x, int))

    def solve_part_2(self, src):
        ls = self.parse(src)
        ans = 0
        mp = defaultdict(int)
        for reg, delta, cond in ls:
            if eval(cond, mp):
                mp[reg] += delta
                ans = max(ans, mp[reg])
        return ans


if __name__ == "__main__":
    sol = Solver17D8()
    session = open('../.session').read().strip()
    cookies = {'session': session}

    src = requests.get(Solver17D8.INPUT_URL, cookies=cookies).text
    print(sol.solve_part_1(src))
    print(sol.solve_part_2(src))
