from itertools import count
from math import lcm

from utils import Solver, get_data


class Solver2023Day8(Solver):
    YEAR = 2023
    DAY = 8
    def __init__(self, src):
        tmp = src.strip().split('\n')
        self.order = tmp[0]
        self.mp = {}
        for s in tmp[2:]:
            now, left, right = ''.join(ch if ch.isalnum() else ' ' for ch in s).split()
            self.mp[now] = (left, right)

    def solve_part_1(self):
        now = 'AAA'
        for i in count():
            if now == 'ZZZ':
                return i
            p = i % len(self.order)
            now = self.mp[now][0] if self.order[p] == 'L' else self.mp[now][1]

    def solve_part_2(self):
        now_list = [k for k in self.mp.keys() if k.endswith('A')]
        ans = 1
        for now in now_list:
            for i in count():
                if now.endswith('Z'):
                    break
                p = i % len(self.order)
                now = self.mp[now][0] if self.order[p] == 'L' else self.mp[now][1]
            ans = lcm(ans, i)
        return ans


if __name__ == "__main__":
    src = get_data(Solver2023Day8.YEAR, Solver2023Day8.DAY)
    sol = Solver2023Day8(src)
    print(sol.solve_part_1())
    print(sol.solve_part_2())
