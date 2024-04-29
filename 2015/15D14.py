import re

import requests

from utils import Solver


class Solver15D14(Solver):
    INPUT_URL = 'https://adventofcode.com/2015/day/14/input'

    def parse(self, src):
        pat = re.compile(r"(\w+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds")
        return [[int(spd), int(t1), int(t2)] for _, spd, t1, t2 in pat.findall(src.strip())]

    def solve_part_1(self, src):
        ls = self.parse(src)
        M = 2503
        return max((M // (t1 + t2) * t1 + min(M % (t1 + t2), t1)) * spd for spd, t1, t2 in ls)

    def solve_part_2(self, src):
        ls = self.parse(src)
        M = 2503
        n = len(ls)
        score = [0 for _ in range(n)]
        dis = [0 for _ in range(n)]
        for i in range(M):
            for j in range(n):
                if i % (ls[j][1] + ls[j][2]) < ls[j][1]:
                    dis[j] += ls[j][0]
            mx = max(dis)
            score = [score[i] + 1 if dis[i] == mx else score[i] for i in range(n)]
        return max(score)


if __name__ == "__main__":
    sol = Solver15D14()
    session = open('../.session').read().strip()
    cookies = {'session': session}
    src = requests.get(Solver15D14.INPUT_URL, cookies=cookies).text
    print(sol.solve_part_1(src))
    print(sol.solve_part_2(src))
