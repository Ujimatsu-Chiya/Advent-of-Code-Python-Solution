import re
from collections import defaultdict, deque

import requests

from utils import Solver


class Solver18D9(Solver):
    INPUT_URL = 'https://adventofcode.com/2018/day/9/input'

    def play_game(self, n, m):
        cnt = [0 for _ in range(n)]
        q = deque([0])

        for i in range(1, m + 1):
            if i % 23 == 0:
                q.rotate(7)
                cnt[i % n] += i + q.pop()
                q.rotate(-1)
            else:
                q.rotate(-1)
                q.append(i)

        return max(cnt)

    def parse(self, src):
        return map(int, re.findall(r'\d+', src.strip()))

    def solve_part_1(self, src):
        n, m = self.parse(src)
        return self.play_game(n, m)

    def solve_part_2(self, src):
        n, m = self.parse(src)
        return self.play_game(n, m * 100)


if __name__ == "__main__":
    sol = Solver18D9()
    session = open('../.session').read().strip()
    cookies = {'session': session}

    src = requests.get(Solver18D9.INPUT_URL, cookies=cookies).text
    print(sol.solve_part_1(src))
    print(sol.solve_part_2(src))
