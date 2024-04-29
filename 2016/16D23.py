import re

import requests

from utils import Solver


class Solver16D23(Solver):
    INPUT_URL = 'https://adventofcode.com/2016/day/23/input'
    dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    pat_mul = re.compile(
        r"cpy (-?\w+) (-?\w+)#inc (-?\w+)#dec \2#jnz \2 (-?\w+)#dec (-?\w+)#jnz \5 (-?\w+)"
    )

    def parse(self, src):
        ls = []
        for s in src.strip().split('\n'):
            ls.append(list(map(lambda t: int(t) if t[-1].isdigit() else t, s.split())))
        return ls

    def _solve(self, vals, ls):
        def get_val(s):
            try:
                return int(s)
            except ValueError:
                return vals[s]

        pos = 0
        while 0 <= pos < len(ls):
            block = "#".join(" ".join(str(t) for t in v) for v in ls[pos:pos + 6])
            if Solver16D23.pat_mul.match(block):
                args = self.pat_mul.findall(block)[0]
                vals[args[2]] += get_val(args[0]) * get_val(args[4])
                vals[args[1]] = vals[args[4]] = 0
                pos += 6
                continue
            ins = ls[pos]
            if ins[0] == "inc":
                vals[ins[1]] += 1
                pos += 1
            elif ins[0] == "dec":
                vals[ins[1]] -= 1
                pos += 1
            elif ins[0] == "cpy":
                vals[ins[2]] = get_val(ins[1])
                pos += 1
            elif ins[0] == "jnz":
                if get_val(ins[1]) != 0:
                    pos += get_val(ins[2])
                else:
                    pos += 1
            else:
                p = pos + get_val(ins[1])
                if 0 <= p < len(ls):
                    if len(ls[p]) == 2:
                        ls[p][0] = ("dec" if ls[p][0] == "inc" else "inc")
                    else:
                        ls[p][0] = ("cpy" if ls[p][0] == "jnz" else "cpy")
                pos += 1
        return vals

    def solve_part_1(self, src):
        ls = self.parse(src)
        vals = {'a': 7}
        return self._solve(vals, ls)['a']

    def solve_part_2(self, src):
        ls = self.parse(src)
        vals = {'a': 12}
        return self._solve(vals, ls)['a']


if __name__ == "__main__":
    sol = Solver16D23()
    session = open('../.session').read().strip()
    cookies = {'session': session}

    src = requests.get(Solver16D23.INPUT_URL, cookies=cookies).text
    print(sol.solve_part_1(src))
    print(sol.solve_part_2(src))
