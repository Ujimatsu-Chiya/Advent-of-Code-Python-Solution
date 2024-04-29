from itertools import count

import requests

from utils import Solver


class Solver17D16(Solver):
    INPUT_URL = 'https://adventofcode.com/2017/day/16/input'

    def parse(self, src):
        ls = []
        for s in src.strip().split(','):
            if s[0] == 's':
                ls.append([s[0], int(s[1:])])
            elif s[0] == 'x':
                A, B = map(int, s[1:].split('/'))
                ls.append([s[0], A, B])
            else:
                A, B = s[1:].split('/')
                ls.append([s[0], A, B])
        return ls

    def _solve(self, ls, s):
        a = list(s)
        for ins in ls:
            if ins[0] == 's':
                a = a[-ins[1]:] + a[:-ins[1]]
            elif ins[0] == 'x':
                x, y = ins[1], ins[2]
                a[x], a[y] = a[y], a[x]
            else:
                c1, c2 = ins[1], ins[2]
                x, y = a.index(c1), a.index(c2)
                a[x], a[y] = a[y], a[x]
        return "".join(a)

    def solve_part_1(self, src):
        ls = self.parse(src)
        s = "abcdefghijklmnop"
        return self._solve(ls, s)

    def solve_part_2(self, src):
        ls = self.parse(src)
        s = "abcdefghijklmnop"
        M = 10 ** 9
        mp = {}
        state_ls = []
        st = T = -1
        for i in count():
            if s in mp.keys():
                T = i - mp[s]
                st = mp[s]
                break
            mp[s] = i
            state_ls.append(s)
            s = self._solve(ls, s)
        if M <= st:
            idx = M
        else:
            idx = st + (M - st) % T
        return state_ls[idx]

if __name__ == "__main__":
    sol = Solver17D16()
    session = open('../.session').read().strip()
    cookies = {'session': session}

    src = requests.get(Solver17D16.INPUT_URL, cookies=cookies).text
    print(sol.solve_part_1(src))
    print(sol.solve_part_2(src))
