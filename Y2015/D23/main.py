from utils import Solver, get_data


class Solver2015Day23(Solver):
    YEAR = 2015
    DAY = 23

    def __init__(self, src):
        self.ls = []
        for s in src.strip().split('\n'):
            s = s.replace(',', ' ')
            self.ls.append(list(map(lambda t: int(t) if t[-1].isdigit() else t, s.split())))

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

    def solve_part_1(self):
        val = {'a': 0, 'b': 0}
        return self._run(val, self.ls)['b']

    def solve_part_2(self):
        val = {'a': 1, 'b': 0}
        return self._run(val, self.ls)['b']


if __name__ == "__main__":
    src = get_data(Solver2015Day23.YEAR, Solver2015Day23.DAY)
    sol = Solver2015Day23(src)
    print(sol.solve_part_1())
    print(sol.solve_part_2())
