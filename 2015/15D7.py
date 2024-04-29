import requests
from queue import Queue
from utils import Solver
from collections import defaultdict


class Solver15D7(Solver):
    INPUT_URL = 'https://adventofcode.com/2015/day/7/input'

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
    sol = Solver15D7()
    session = open('../.session').read().strip()
    cookies = {'session': session}
    src = requests.get(Solver15D7.INPUT_URL, cookies=cookies).text
    print(sol.solve_part_1(src))
    print(sol.solve_part_2(src))
