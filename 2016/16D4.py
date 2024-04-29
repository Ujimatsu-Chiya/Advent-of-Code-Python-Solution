import re

import requests

from utils import Solver
from collections import Counter


class Solver16D4(Solver):
    INPUT_URL = 'https://adventofcode.com/2016/day/4/input'

    def parse(self, src):
        pat = re.compile(r'(.+)-(\d+)\[(.+)\]')
        ls = pat.findall(src.strip())
        return [[s[0], int(s[1]), s[2]] for s in ls]

    def solve_part_1(self, src):
        ls = self.parse(src)
        ans = 0
        for s, id, check_sum in ls:
            a = sorted((-v, k) for k, v in Counter(s.replace('-','')).items())
            check = "".join(v[1] for v in a[:5])
            if check == check_sum:
                ans += id
        return ans

    def solve_part_2(self, src):
        ls = self.parse(src)
        for s, id, _ in ls:
            s = "".join([chr((ord(ch)-ord('a') + id) % 26 + ord('a')) if ch.isalpha() else ch for ch in s]).replace('-', ' ')
            if s == 'northpole object storage':
                return id


if __name__ == "__main__":
    sol = Solver16D4()
    session = open('../.session').read().strip()
    cookies = {'session': session}
    src = requests.get(Solver16D4.INPUT_URL, cookies=cookies).text
    print(sol.solve_part_1(src))
    print(sol.solve_part_2(src))
