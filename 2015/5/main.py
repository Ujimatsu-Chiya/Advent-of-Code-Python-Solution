from collections import defaultdict

from utils import Solver, get_data


class Solver2015Day5(Solver):
    YEAR = 2015
    DAY = 5

    def parse(self, src):
        return src.strip().split()

    def solve_part_1(self, src):
        ls = self.parse(src)
        lt = 'ab', 'cd', 'pq', 'xy'
        st = 'aeiou'
        ans = 0
        for s in ls:
            if len([ch for ch in s if ch in st]) >= 3 and \
                    any(s[i] == s[i + 1] for i in range(len(s) - 1)) and \
                    not any(t in s for t in lt):
                ans += 1
        return ans

    def solve_part_2(self, src):
        ls = self.parse(src)
        ans = 0
        for s in ls:
            mp = defaultdict(list)
            for i in range(len(s) - 1):
                mp[s[i:i + 2]].append(i)
            if any(len(v) > 2 or len(v) == 2 and v[1] - v[0] > 1 for v in mp.values()) and \
                    any(s[i] == s[i + 2] for i in range(len(s) - 2)):
                ans += 1
        return ans


if __name__ == "__main__":
    sol = Solver2015Day5()
    src = get_data(Solver2015Day5.YEAR, Solver2015Day5.DAY)
    print(sol.solve_part_1(src))
    print(sol.solve_part_2(src))

