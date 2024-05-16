from collections import Counter

from utils import Solver, get_data


class Solver2023Day7(Solver):
    YEAR = 2023
    DAY = 7

    def __init__(self, src):
        tmp = src.strip().split('\n')
        ls = []
        for s in tmp:
            s, val = s.split()
            ls.append((s, int(val)))
        return ls

    def _get_rank_1(self, s):
        v = sorted(Counter(s).values())
        if v[-1] == 5:
            return 7
        elif v[-1] == 4:
            return 6
        elif v[-1] == 3:
            return 5 if len(v) == 2 else 4
        elif v[-1] == 2:
            return 3 if v.count(2) == 2 else 2
        else:
            return 1

    def _get_rank_2(self, s):
        c = Counter(s.replace('J', ''))
        v = sorted(c.values())
        if len(v) == 0:
            return 7
        t = s.replace('J', max(c, key=c.get))
        return self._get_rank_1(t)

    def solve_part_1(self):
        ls = self.parse(src)
        s = '23456789TJQKA'
        mp = {ch: i for i, ch in enumerate(s)}
        lt = sorted([([self._get_rank_1(s)] + [mp[ch] for ch in s], val) for s, val in ls])
        ans = sum((i + 1) * v[1] for i, v in enumerate(lt))
        return ans

    def solve_part_2(self):
        ls = self.parse(src)
        s = 'J23456789TQKA'
        mp = {ch: i for i, ch in enumerate(s)}
        lt = sorted([([self._get_rank_2(s)] + [mp[ch] for ch in s], val) for s, val in ls])
        ans = sum((i + 1) * v[1] for i, v in enumerate(lt))
        return ans


if __name__ == "__main__":
    sol = Solver2023Day7()
    src = get_data(Solver2023Day7.YEAR, Solver2023Day7.DAY)
    print(sol.solve_part_1())
    print(sol.solve_part_2())
