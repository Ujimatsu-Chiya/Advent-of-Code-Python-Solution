import requests

from utils import Solver


class Solver15D23(Solver):
    INPUT_URL = 'https://adventofcode.com/2015/day/23/input'

    def parse(self, src):
        ls = []
        for s in src.strip().split('\n'):
            s = s.replace(',', ' ')
            ls.append(list(map(lambda t: int(t) if t[-1].isdigit() else t, s.split())))
        return ls

    def _run(self, val, ls):
        pos = 0
        while 0 <= pos < len(ls):
            ins = ls[pos]
            if ins[0] == 'hlf':
                val[ins[1]] >>= 1
                pos += 1
            elif ins[0] == 'tpl':
                val[ins[1]] *= 3
                pos += 1
            elif ins[0] == 'inc':
                val[ins[1]] += 1
                pos += 1
            elif ins[0] == 'jmp':
                pos += ins[1]
            elif ins[0] == 'jie':
                if val[ins[1]] % 2 == 0:
                    pos += ins[2]
                else:
                    pos += 1
            elif ins[0] == 'jio':
                if val[ins[1]] == 1:
                    pos += ins[2]
                else:
                    pos += 1
            else:
                assert False
        return val

    def solve_part_1(self, src):
        ls = self.parse(src)
        val = {'a': 0, 'b': 0}
        return self._run(val, ls)['b']

    def solve_part_2(self, src):
        ls = self.parse(src)
        val = {'a': 1, 'b': 0}
        return self._run(val, ls)['b']


if __name__ == "__main__":
    sol = Solver15D23()
    session = open('../.session').read().strip()
    cookies = {'session': session}
    src = requests.get(Solver15D23.INPUT_URL, cookies=cookies).text
    print(sol.solve_part_1(src))
    print(sol.solve_part_2(src))
