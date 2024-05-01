from utils import Solver, get_data


class Solver2016Day12(Solver):
    YEAR = 2016
    DAY = 12

    def parse(self, src):
        ls = []
        for s in src.strip().split('\n'):
            ls.append(list(map(lambda t: int(t) if t[-1].isdigit() else t, s.split())))
        return ls

    def _run(self, val, ls):
        pos = 0
        while 0 <= pos < len(ls):
            ins = ls[pos]
            if ins[0] == 'cpy':
                if isinstance(ins[1], int):
                    val[ins[2]] = ins[1]
                else:
                    val[ins[2]] = val[ins[1]]
                pos += 1
            elif ins[0] == 'inc':
                val[ins[1]] += 1
                pos += 1
            elif ins[0] == 'dec':
                val[ins[1]] -= 1
                pos += 1
            elif ins[0] == 'jnz':
                if isinstance(ins[1], int) and ins[1] != 0 or not isinstance(ins[1], int) and val[ins[1]] != 0:
                    pos += ins[2]
                else:
                    pos += 1
        return val

    def solve_part_1(self, src):
        ls = self.parse(src)
        val = {ch: 0 for ch in 'abcd'}
        return self._run(val, ls)['a']

    def solve_part_2(self, src):
        ls = self.parse(src)
        val = {ch: 0 for ch in 'abd'}
        val['c'] = 1
        return self._run(val, ls)['a']


if __name__ == "__main__":
    sol = Solver2016Day12()
    src = get_data(Solver2016Day12.YEAR, Solver2016Day12.DAY)
    print(sol.solve_part_1(src))
    print(sol.solve_part_2(src))
