import requests

from utils import Solver


class Solver23D15(Solver):
    INPUT_URL = 'https://adventofcode.com/2023/day/15/input'

    def parse(self, src):
        return src.strip().split(',')

    def solve_part_1(self, src):
        ls = self.parse(src)
        ans = 0
        for s in ls:
            w = 0
            for ch in s:
                w = (w + ord(ch)) * 17 % 256
            ans += w
        return ans

    def solve_part_2(self, src):
        ls = self.parse(src)
        mp = {}
        for i, s in enumerate(ls):
            if s.endswith('-'):
                tag = s.rstrip('-')
                if tag in mp.keys():
                    mp.pop(tag)
            else:
                tag, idx = s.split('=')
                idx = int(idx)
                if tag in mp.keys():
                    mp[tag] = (idx, mp[tag][1])
                else:
                    mp[tag] = (idx, i)
        M = 256
        box = [[] for _ in range(M)]
        for tag, t in mp.items():
            w = 0
            for ch in tag:
                w = (w + ord(ch)) * 17 % 256
            if len(t) > 0:
                idx, tm = t
                box[w].append((tm, idx, tag))
        ans = 0
        for id, b in enumerate(box):
            b.sort()
            for j in range(len(b)):
                ans += (id + 1) * (j + 1) * b[j][1]
        return ans


if __name__ == "__main__":
    sol = Solver23D15()
    session = open('../.session').read().strip()
    cookies = {'session': session}
    src = requests.get(Solver23D15.INPUT_URL, cookies=cookies).text
    print(sol.solve_part_1(src))
    print(sol.solve_part_2(src))
