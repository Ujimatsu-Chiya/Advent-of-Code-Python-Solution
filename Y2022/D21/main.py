from collections import defaultdict
from fractions import Fraction
from queue import Queue

from utils import Solver, get_data


class Solver2022Day21(Solver):
    YEAR = 2022
    DAY = 21

    def __init__(self, src):
        # src = src.replace('/', '//')
        self.mp = {}
        for s in src.strip().split('\n'):
            wire, exp = s.split(': ')
            self.mp[wire] = exp
        self.ans1 = self.ans2 = None

    def _run(self, mp):
        vals = {}
        deg = defaultdict(int)
        g = defaultdict(list)
        q = Queue()
        for wire, exp in self.mp.items():
            if exp.isdigit():
                q.put(wire)
            elif exp.count(' ') == 0:
                deg[wire] = 1
                g[exp] = wire
            else:
                exp_list = exp.split()
                var_list = [exp_list[0], exp_list[2]]
                for u in var_list:
                    if u.isalpha():
                        g[u].append(wire)
                        deg[wire] += 1
        while q.qsize() > 0:
            wire = q.get()
            vals[wire] = Fraction(eval(mp[wire], vals))
            for nxt in g[wire]:
                deg[nxt] -= 1
                if deg[nxt] == 0:
                    q.put(nxt)
        return vals

    def solve_part_1(self):
        return int(self._run(self.mp)['root'])

    def solve_part_2(self):
        ls = []
        for s in range(5):
            self.mp['humn'] = str(s)
            res = self._run(self.mp)
            exp = self.mp['root']
            exp_list = exp.split()
            var_list = [exp_list[0], exp_list[2]]
            ls.append([res[var_list[0]], res[var_list[1]]])
        if ls[0][0] == ls[1][0]:
            ls = [u[::-1] for u in ls]
        step = ls[1][0] - ls[0][0]
        dis = ls[0][1] - ls[0][0]
        return int(dis / step)

if __name__ == "__main__":
    src = get_data(Solver2022Day21.YEAR, Solver2022Day21.DAY)
    sol = Solver2022Day21(src)
    print(sol.solve_part_1())
    print(sol.solve_part_2())
