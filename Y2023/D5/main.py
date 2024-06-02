from math import inf

from utils import Solver, get_data


class Solver2023Day5(Solver):
    YEAR = 2023
    DAY = 5

    def __init__(self, src):
        seed_str, *map_str = src.strip().split('\n\n')
        self.seeds = list(map(int, seed_str.split(':')[1].split()))
        self.maps = [[list(map(int, t.split())) for t in s.split('\n')[1:]] for s in map_str]

    def solve_part_1(self):
        def evaluate(f, x):
            for dst_pos, src_pos, l in f:
                if src_pos <= x < src_pos + l:
                    return dst_pos + (x - src_pos)
            return x

        ans = []
        for x in self.seeds:
            for f in self.maps:
                x = evaluate(f, x)
            ans.append(x)
        return min(ans)

    def solve_part_2(self):
        x = []
        for i in range(0, len(self.seeds), 2):
            x.append((self.seeds[i], self.seeds[i] + self.seeds[i + 1]))
        for f in self.maps:
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
    src = get_data(Solver2023Day5.YEAR, Solver2023Day5.DAY)
    sol = Solver2023Day5(src)
    print(sol.solve_part_1())
    print(sol.solve_part_2())
