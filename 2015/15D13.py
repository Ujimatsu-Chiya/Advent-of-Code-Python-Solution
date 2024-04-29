import re
from itertools import permutations

import requests

from utils import Solver


class Solver15D13(Solver):
    INPUT_URL = 'https://adventofcode.com/2015/day/13/input'

    def parse(self, src):
        pat = re.compile(r"(\w+) would (lose|gain) (\d+) happiness units by sitting next to (\w+)\.")
        return [[p1, p2, int(v) if op == 'gain' else -int(v)] for p1, op, v, p2 in pat.findall(src.strip())]

    def solve_part_1(self, src):
        ls = self.parse(src)
        mp = {}
        st = set()
        for x, y, w in ls:
            mp[x, y] = w
            st |= {x, y}
        ls = list(st)
        lt, ls = ls[:1], ls[1:]
        ans = 0
        n = len(st)
        for p in permutations(ls):
            t = lt + list(p) + lt
            ans = max(ans, sum(mp[t[i], t[i + 1]] + mp[t[i + 1], t[i]] for i in range(n)))
        return ans

    def solve_part_2(self, src):
        ls = self.parse(src)
        mp = {}
        st = set()
        for x, y, w in ls:
            mp[x, y] = w
            st |= {x, y}
        me = 'me'
        for s in st:
            mp[s, me] = mp[me, s] = 0
        st.add(me)
        ls = list(st)
        lt, ls = ls[:1], ls[1:]
        ans = 0
        n = len(st)
        for p in permutations(ls):
            t = lt + list(p) + lt
            ans = max(ans, sum(mp[t[i], t[i + 1]] + mp[t[i + 1], t[i]] for i in range(n)))
        return ans


if __name__ == "__main__":
    sol = Solver15D13()
    session = open('../.session').read().strip()
    cookies = {'session': session}
    src = requests.get(Solver15D13.INPUT_URL, cookies=cookies).text

    print(sol.solve_part_1(src))
    print(sol.solve_part_2(src))
