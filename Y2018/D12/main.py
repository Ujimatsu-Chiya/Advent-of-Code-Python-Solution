import re
from itertools import count

from utils import Solver, get_data


class Solver2018Day12(Solver):
    YEAR = 2018
    DAY = 12

    def __init__(self, src):
        pat = re.compile(r'([.#]{5}) => ([.#])')
        self.mp = {}
        for l, r in pat.findall(src.strip()):
            tp = tuple(i - 2 for i in range(len(l)) if l[i] == '#')
            self.mp[tp] = (r == '#')
        s = re.search(r'initial state: ([.#]+)', src.strip()).group(1)
        self.s = set(i for i in range(len(s)) if s[i] == '#')
        self.ans1 = self.ans2 = None

    def run(self):
        s, mp = self.s, self.mp
        state_ls = []
        st = T = d = -1
        for i in count():
            a = sorted(s)
            tp = tuple(a[i + 1] - a[i] for i in range(len(a) - 1))
            if tp in mp.keys():
                T = i - mp[tp][0]
                st = mp[tp][0]
                d = a[0] - mp[tp][1][0]
                break
            mp[tp] = i, a
            state_ls.append(a)
            l, r = min(s), max(s)
            t = set()
            for i in range(l - 2, r + 2 + 1):
                tp = tuple(d for d in range(-2, 3) if i + d in s)
                if mp[tp]:
                    t.add(i)
            s = t

        def que(M):
            if st >= M:
                return state_ls[M]
            else:
                q, m = divmod(M - st, T)
                idx = st + m
                return [q * d + state_ls[idx][i] for i in range(len(state_ls[idx]))]

        self.ans1 = sum(que(20))
        self.ans2 = sum(que(50000000000))

    def solve_part_1(self):
        return self.ans1

    def solve_part_2(self):
        return self.ans2


if __name__ == "__main__":
    src = get_data(Solver2018Day12.YEAR, Solver2018Day12.DAY)
    sol = Solver2018Day12(src)
    sol.run()
    print(sol.solve_part_1())
    print(sol.solve_part_2())
