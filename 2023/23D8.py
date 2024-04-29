import requests
from itertools import count
from math import lcm

from utils import Solver


class Solver23D8(Solver):
    INPUT_URL = 'https://adventofcode.com/2023/day/8/input'
    def parse(self, src):
        tmp = src.strip().split('\n')
        order = tmp[0]
        mp = {}
        for s in tmp[2:]:
            now, left, right = ''.join(ch if ch.isalnum() else ' ' for ch in s).split()
            mp[now] = (left, right)
        return order, mp

    def solve_part_1(self, src):
        order, mp = self.parse(src)
        now = 'AAA'
        for i in count():
            if now == 'ZZZ':
                return i
            p = i % len(order)
            now = mp[now][0] if order[p] == 'L' else mp[now][1]

    def solve_part_2(self, src):
        order, mp = self.parse(src)
        now_list = [k for k in mp.keys() if k.endswith('A')]
        ans = 1
        for now in now_list:
            for i in count():
                if now.endswith('Z'):
                    break
                p = i % len(order)
                now = mp[now][0] if order[p] == 'L' else mp[now][1]
            ans = lcm(ans, i)
        return ans


if __name__ == "__main__":
    sol = Solver23D8()
    session = open('../.session').read().strip()
    cookies = {'session': session}
    src = requests.get(Solver23D8.INPUT_URL, cookies=cookies).text
    print(sol.solve_part_1(src))
    print(sol.solve_part_2(src))
