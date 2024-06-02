from collections import defaultdict
from queue import Queue

from utils import Solver, get_data
from keyword import kwlist

class Solver2015Day7(Solver):
    YEAR = 2015
    DAY = 7

    def __init__(self, src):
        msk = (1 << 16) - 1
        src = src.replace('LSHIFT', '<<').replace('RSHIFT', '>>'). \
            replace('AND', '&').replace('OR', '|').replace('NOT', '{} ^'.format(msk))
        for keyword in kwlist:
            src = src.replace(keyword, keyword * 2)
        self.mp = {}
        for s in src.strip().split('\n'):
            exp, wire = s.split(' -> ')
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
            vals[wire] = eval(mp[wire], vals)
            for nxt in g[wire]:
                deg[nxt] -= 1
                if deg[nxt] == 0:
                    q.put(nxt)
        return vals

    def run(self):
        vals = self._run(self.mp)
        self.ans1 = vals['a']
        self.mp['b'] = str(vals['a'])
        vals = self._run(self.mp)
        self.ans2 = vals['a']

    def solve_part_1(self):
        return self.ans1

    def solve_part_2(self):
        return self.ans2


if __name__ == "__main__":
    src = get_data(Solver2015Day7.YEAR, Solver2015Day7.DAY)
    sol = Solver2015Day7(src)
    sol.run()
    print(sol.solve_part_1())
    print(sol.solve_part_2())