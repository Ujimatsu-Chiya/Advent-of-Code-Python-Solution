from collections import defaultdict
from queue import Queue

from utils import Solver, get_data


class Solver2015Day7(Solver):
    YEAR = 2015
    DAY = 7

    def parse(self, src):
        msk = (1 << 16) - 1
        src = src.replace('LSHIFT', '<<').replace('RSHIFT', '>>'). \
            replace('AND', '&').replace('OR', '|').replace('NOT', '{} ^'.format(msk))
        for keyword in ['as', 'if', 'in', 'is']:
            src = src.replace(keyword, keyword * 2)
        mp = {}
        for s in src.strip().split('\n'):
            exp, wire = s.split(' -> ')
            mp[wire] = exp
        return mp

    def solve_part_1(self, src):
        mp = self.parse(src)
        vals = {}
        deg = defaultdict(int)
        g = defaultdict(list)
        q = Queue()

        for wire, exp in mp.items():
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
        return vals['a']

    def solve_part_2(self, src):
        x = self.solve_part_1(src)
        mp = self.parse(src)
        src = src.replace("{} -> b".format(mp['b']), '{} -> b'.format(x))
        return self.solve_part_1(src)


if __name__ == "__main__":
    sol = Solver2015Day7()
    src = get_data(Solver2015Day7.YEAR, Solver2015Day7.DAY)
    print(sol.solve_part_1(src))
    print(sol.solve_part_2(src))
