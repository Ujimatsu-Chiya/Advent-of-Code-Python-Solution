import requests

from utils import Solver


class Solver17D5(Solver):
    INPUT_URL = 'https://adventofcode.com/2017/day/5/input'

    def parse(self, src):
        return list(map(int, src.strip().split()))

    def solve_part_1(self, src):
        a = self.parse(src)
        p = 0
        cnt = 0
        while 0 <= p < len(a):
            x = a[p]
            a[p] += 1
            p += x
            cnt += 1
        return cnt

    def solve_part_2(self, src):
        a = self.parse(src)
        p = 0
        cnt = 0
        while 0 <= p < len(a):
            x = a[p]
            a[p] = a[p] - 1 if a[p] >= 3 else a[p] + 1
            p += x
            cnt += 1
        return cnt

if __name__ == "__main__":
    sol = Solver17D5()
    session = open('../.session').read().strip()
    cookies = {'session': session}

    src = requests.get(Solver17D5.INPUT_URL, cookies=cookies).text
    print(sol.solve_part_1(src))
    print(sol.solve_part_2(src))
