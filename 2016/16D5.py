import hashlib
from itertools import count

import requests

from utils import Solver


class Solver16D5(Solver):
    INPUT_URL = 'https://adventofcode.com/2016/day/5/input'

    def parse(self, src):
        return src.strip()

    def solve_part_1(self, src):
        s = self.parse(src)
        ans = ''
        prefix = "00000"
        for i in count(1):
            md5 = hashlib.md5((s + str(i)).encode())
            t = md5.hexdigest()
            if t.startswith(prefix):
                ans += t[len(prefix)]
                if len(ans) == 8:
                    break
        return ans

    def solve_part_2(self, src):
        s = self.parse(src)
        M = 8
        ans = ['' for _ in range(M)]
        prefix = "00000"
        cnt = 0
        for i in count(1):
            md5 = hashlib.md5((s + str(i)).encode())
            t = md5.hexdigest()
            if t.startswith(prefix):
                c1, c2 = t[len(prefix)], t[len(prefix) + 1]
                if c1.isdigit():
                    p = int(c1)
                    if p < M and ans[p] == '':
                        ans[p] = c2
                        cnt += 1
                        if cnt == M:
                            break
        return ''.join(ans)


if __name__ == "__main__":
    sol = Solver16D5()
    session = open('../.session').read().strip()
    cookies = {'session': session}
    src = requests.get(Solver16D5.INPUT_URL, cookies=cookies).text
    print(sol.solve_part_1(src))
    print(sol.solve_part_2(src))