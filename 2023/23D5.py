from math import inf

import requests

from utils import Solver


class Solver23D5(Solver):
    INPUT_URL = 'https://adventofcode.com/2023/day/5/input'

    def parse(self, src):
        ls = src.strip().split('\n')
        seeds = list(map(int, ls[0].split(':')[1].split()))
        maps = []
        i = 1
        while i < len(ls):
            if 'map' not in ls[i]:
                i += 1
                continue
            j = i + 1
            f = []
            while j < len(ls) and len(ls[j]) > 0:
                f.append(list(map(int, ls[j].split())))
                j += 1
            maps.append(f)
            i = j
        return seeds, maps

    def solve_part_1(self, src):
        def evaluate(f, x):
            for dst_pos, src_pos, l in f:
                if src_pos <= x < src_pos + l:
                    return dst_pos + (x - src_pos)
            return x

        seed, maps = self.parse(src)
        ans = []
        for x in seed:
            for f in maps:
                x = evaluate(f, x)
            ans.append(x)
        return min(ans)

    def solve_part_2(self, src):
        tmp, maps = self.parse(src)
        x = []
        for i in range(0, len(tmp), 2):
            x.append((tmp[i], tmp[i] + tmp[i + 1]))
        for f in maps:
            f = sorted(f, key=lambda v: v[1])
            normal_f = {}
            for dst_pos, src_pos, l in f:
                normal_f[src_pos, src_pos + l] = dst_pos - src_pos
            for i in range(len(f) - 1):
                if f[i][1] + f[i][2] < f[i + 1][1]:
                    normal_f[f[i][1] + f[i][2], f[i + 1][1]] = 0
            normal_f[-inf, f[0][1]] = normal_f[f[-1][1] + f[-1][2], inf] = 0
            tmp = []
            for l1, r1 in x:
                for pa, delta in normal_f.items():
                    l2, r2 = pa
                    l, r = max(l1, l2), min(r1, r2)
                    if l < r:
                        tmp.append((l + delta, r + delta))
            tmp.sort()
            x = []
            for l, r in tmp:
                if len(x) == 0 or l > x[-1][1]:
                    x.append([l, r])
                else:
                    x[-1][1] = r
        return x[0][0]


if __name__ == "__main__":
    sol = Solver23D5()
    session = open('../.session').read().strip()
    cookies = {'session': session}
    src = requests.get(Solver23D5.INPUT_URL, cookies=cookies).text
    print(sol.solve_part_1(src))
    print(sol.solve_part_2(src))
