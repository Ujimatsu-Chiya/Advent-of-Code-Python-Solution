import requests

from utils import Solver
from collections import defaultdict


class Solver15D5(Solver):
    INPUT_URL = 'https://adventofcode.com/2015/day/5/input'

    def parse(self, src):
        return src.strip().split()

    def solve_part_1(self, src):
        ls = self.parse(src)
        lt = 'ab', 'cd', 'pq', 'xy'
        st = 'aeiou'
        ans = 0
        for s in ls:
            if len([ch for ch in s if ch in st]) >= 3 and \
                    any(s[i] == s[i + 1] for i in range(len(s) - 1)) and \
                    not any(t in s for t in lt):
                ans += 1
        return ans

    def solve_part_2(self, src):
        ls = self.parse(src)
        ans = 0
        for s in ls:
            mp = defaultdict(list)
            for i in range(len(s) - 1):
                mp[s[i:i + 2]].append(i)
            if any(len(v) > 2 or len(v) == 2 and v[1] - v[0] > 1 for v in mp.values()) and \
                    any(s[i] == s[i + 2] for i in range(len(s) - 2)):
                ans += 1
        return ans


if __name__ == "__main__":
    sol = Solver15D5()
    session = open('../.session').read().strip()
    cookies = {'session': session}
    src = requests.get(Solver15D5.INPUT_URL, cookies=cookies).text
    print(sol.solve_part_1(src))
    print(sol.solve_part_2(src))
